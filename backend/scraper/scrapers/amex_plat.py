"""
American Express Platinum Card Scraper
- Scrapes the benefits of the Amex Plat Card from https://www.americanexpress.com/us/credit-cards/card/platinum/
- Processes the raw text of each benefit entry into structured data
- Stores the structured data in Redis
"""

from playwright.sync_api import sync_playwright

class AmexPlatScraper():
    def __init__(self):
        super().__init__()
        self.url = 'https://www.americanexpress.com/us/credit-cards/card/platinum/'

    def scrape(self):
        """
        Scrapes the Amex Plat card benefits and stores them in Redis
        """
        # Launch browser
        with sync_playwright() as p:
            # Launch the browser
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Navigate to the page
            page.goto(self.url)

            # Wait for benefits section to load
            page.wait_for_selector("div.axp-shop-us-consumer__index__howYouEarn___3Y3ia", state='attached')

            # Extract the benefits section
            first_div = page.query_selector('div.axp-shop-us-consumer__index__howYouEarn___3Y3ia')
            li_elements = first_div.query_selector_all('li') if first_div else []

            # Parse benefits section
            rewards = []
            for li in li_elements:
                text = li.text_content()
                if text:
                    rewards.append(text.strip())

            print("Extracted items:")
            for item in rewards:
                print("-", item)

            browser.close()

if __name__ == "__main__":
    AmexPlatScraper().scrape()