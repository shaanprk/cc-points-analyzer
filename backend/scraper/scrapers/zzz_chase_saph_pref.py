"""
Chase Sapphire Preferred
- Scrapes the benefits of the Chase Sapphire Preferred Card
"""

from base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from contextlib import suppress
import json
import re

class ChaseSapphirePreferredScraper(BaseScraper):
    def __init__(self):
        super().__init__()
        self.url = 'https://creditcards.chase.com/a1/24Q4/sapphirepreferred?CELL=6H8X'
        self.xpath_expr = "//section[contains(@class, 'section-earn')]//div[contains(@class, 'slick-track')]//div[contains(@class, 'slick-slide') and not(contains(@class, 'slick-cloned'))]"
    
    def scrape(self):
        try:
            self.load_page(self.url)
            benefits = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, self.xpath_expr))
            )

            def process_raw_text(raw_text):
                lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

                multiplier_match = re.search(r'(\d+x)', raw_text)
                if not multiplier_match:
                    return None

                multiplier = multiplier_match.group(1)

                try:
                    title_index = lines.index(multiplier)
                    title = lines[title_index]

                    conditions_arr = []
                    title_finished = False
                    for line in lines[title_index + 1:]:
                        if "offer details Opens overlay" in line or "Offer details Opens overlay" in line:
                            pass
                        elif not line.startswith('Earn') and not title_finished:
                            title = title + " " + line
                        else:
                            title_finished = True
                            conditions_arr.append(line)
                    conditions = ' '.join(conditions_arr)
                except (ValueError, IndexError):
                    return None


                return {
                    "Title": title,
                    "Multiplier": multiplier,
                    "Conditions": conditions,
                }
            
            benefits_data = []

            # Extract and process each benefit
            for benefit in benefits:
                raw_text = benefit.get_attribute("innerText")
                benefit_info = process_raw_text(raw_text)
                if benefit_info:
                    benefits_data.append(benefit_info)

            # Write to external file
            with open("chase_sapphire_preferred_benefits.json", "w", encoding="utf-8") as f:
                json.dump(benefits_data, f, indent=4, ensure_ascii=False)
        
        finally:
            with suppress(Exception):
                self.quit_driver()