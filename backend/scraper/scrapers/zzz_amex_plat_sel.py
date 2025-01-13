"""
Amex Plat Scraper
- Scrapes the benefits of the Amex Plat Card
"""

from base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from contextlib import suppress
import json

class AmexPlatScraper(BaseScraper):
    def __init__(self):
        super().__init__()
        self.url = 'https://www.americanexpress.com/us/credit-cards/card/platinum/'
        self.xpath_exp = '//*[@id="root"]/div[7]/div/div[2]/div/div/div/div/div[2]/div[6]/div/div/div/section/ul/li/div'

    def scrape(self):
        try:
            self.load_page(self.url)
            benefits = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, self.xpath_expr))
            )

            def process_raw_text(raw_text):
                lines = [line.strip() for line in raw_text.split("\n") if line.strip()]
                if len(lines) < 3:
                    return None

                title = lines[0]
                multiplier = lines[1]
                conditions = " ".join(lines[3:]) if len(lines) > 3 else ""

                return {
                    "Title:": title,
                    "Multiplier": multiplier,
                    "Conditions": conditions
                }

            benefits_data = []

            for benefit in benefits:
                raw_text = benefit.get_atrribute("innertext")
                benefit_info = process_raw_text(raw_text)
                if benefit_info:
                    benefits_data.append(benefit_info)
                
            with open("amex_plat_benefits.json", "w", encoding="utf-8") as f:
                json.dump(benefits_data, f, indent=4, ensure_ascii=False)
            
        finally:
            with suppress(Exception):
                self.quit_driver()