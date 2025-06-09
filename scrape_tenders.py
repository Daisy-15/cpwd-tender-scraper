import csv
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

csv_cols = {
    "NIT/RFP NO": "ref_no",
    "Name of Work / Subwork / Packages": "title",
    "Estimated Cost": "tender_value",
    "Bid Submission Closing Date & Time": "bid_submission_end_date",
    "EMD Amount": "emd",
    "Bid Opening Date & Time": "bid_open_date"
}
def clean_text(text):
    return text.replace('\n', ' ').replace('\r', ' ').strip()

def convert_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return date_str

def scrape_tenders():
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 30)

    driver.get("https://etender.cpwd.gov.in/")

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "New Tenders"))).click()
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "All"))).click()
    time.sleep(3)

    length_select_element = wait.until(EC.element_to_be_clickable((By.NAME, "awardedDataTable_length")))
    select = Select(length_select_element)
    select.select_by_visible_text('20')

    wait.until(EC.invisibility_of_element_located((By.ID, "awardedDataTable_processing")))

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#awardedDataTable tbody tr")))

    rows = driver.find_elements(By.CSS_SELECTOR, "#awardedDataTable tbody tr")

    tenders = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 6:
            tenders.append({
                csv_cols["NIT/RFP NO"]: clean_text(cells[1].text),
                csv_cols["Name of Work / Subwork / Packages"]: clean_text(cells[2].text),
                csv_cols["Estimated Cost"]: clean_text(cells[4].text),
                csv_cols["Bid Submission Closing Date & Time"]: clean_text(convert_date(cells[6].text)),
                csv_cols["EMD Amount"]: clean_text(cells[5].text),
                csv_cols["Bid Opening Date & Time"]: clean_text(convert_date(cells[7].text))
            })

    driver.quit()

    with open("tenders.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=csv_cols.values())
        writer.writeheader()
        writer.writerows(tenders)


    print(f"Scraping complete. Rows fetched: {len(tenders)}. Data saved in tenders.csv")

if __name__ == "__main__":
    scrape_tenders()
