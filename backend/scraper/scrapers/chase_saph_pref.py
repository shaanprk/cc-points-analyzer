"""
Chase Sapphire Preferred Scraper
- Scrapes the benefits of the Chase Sapphire Preferred Card from https://creditcards.chase.com/a1/24Q4/sapphirepreferred?CELL=6H8X
- Processes the raw text of each benefit entry into structured data
- Stores the structured data in Redis
"""

from playwright.sync_api import sync_playwright

class ChaseSaphPrefScraper():
    def __init__(self):
        super().__init__()
        self.url = 'https://creditcards.chase.com/a1/24Q4/sapphirepreferred?CELL=6H8X'

    def scrape(self):
        """
        Scrapes the Chase Sapphire Preferred card benefits and stores them in Redis
        """
        # Launch browser
        with sync_playwright() as p:
            # Launch the browser
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Navigate to the page
            page.goto(self.url, wait_until="domcontentloaded")

            # Wait for benefits section to load
            page.wait_for_selector("section.section-earn", state='attached')

            # Extract the benefits section
            benefits = page.query_selector_all('section.section-earn div.slick-slide:not(.slick-cloned) h4')

            # Parse benefits section
            rewards = []
            for benefit in benefits:
                text = benefit.text_content()
                if text:
                    rewards.append(text.strip())

            print("Extracted items:")
            for item in rewards:
                print("-", item)

            browser.close()

if __name__ == "__main__":
    ChaseSaphPrefScraper().scrape()