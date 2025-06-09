# cpwd-tender-scraper
A Python script that automates the extraction of tender data from the official CPWD e-Tendering website: [https://etender.cpwd.gov.in/](https://etender.cpwd.gov.in/). It navigates to the "New Tenders" section, selects the "All" tab, scrapes details of the first 20 tenders, and saves the data in a CSV file with structured columns for easy analysis.

---

Features

- Navigates to the "New Tenders" → "All" tab.
- Extracts details of the first 20 tenders listed.
- Scrapes the following fields:
  - NIT/RFP NO
  - Name of Work / Subwork / Packages
  - Estimated Cost
  - Bid Submission Closing Date & Time
  - EMD Amount
  - Bid Opening Date & Time
- Cleans and formats the scraped data.
- Saves data into a CSV file (tenders.csv).

---

Requirements

- Python 3.7+
- Google Chrome browser
- Matching version of ChromeDriver
- Python packages listed in requirements.txt

---

Setup & Usage

1. Clone this repository:
   git clone https://github.com/yourusername/cpwd-tender-scraper.git
   cd cpwd-tender-scraper

2. Install dependencies:
   pip install -r requirements.txt

3. Download and place the correct version of chromedriver executable for your OS in the project directory or update PATH.

4. Launch Chrome with remote debugging enabled:
   chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeProfile"
   (Adjust command as per your OS and Chrome path)

5. Run the scraper:
   python scraper.py

6. The scraped data will be saved to tenders.csv.

---

Notes

- Ensure ChromeDriver version matches your installed Chrome browser version.
- The scraper uses Selenium and Chrome’s remote debugging protocol.
- Modify selectors in the script if the website structure changes.
