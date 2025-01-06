"""
Amex Gold Scraper
- Scrapes the benefits of the Amex Gold Card
"""

from base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from contextlib import suppress
import json
import redis

class AmexGoldScraper(BaseScraper):
    redis_client = redis.StrictRedis(
        host = 'localhost',
        port= 6380,
        db= 0,
        # decode_responses=True
    )

    def __init__(self):
        super().__init__()
        self.url = 'https://www.americanexpress.com/us/credit-cards/card/gold-card/'
        self.xpath_expr = '//*[@id="root"]/div[5]/div/div[2]/div/div/div/div/div[2]/div[5]/div/div/div/section/ul/li/div'
    

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

            # for benefit in benefits:
            #     raw_text = benefit.get_attribute("innertext")
            #     benefit_info = process_raw_text(raw_text)
            #     if benefit_info:
            #         benefits_data.append(benefit_info)
            
            # Save as JSON file
            # with open("amex_gold_benefits.json", "w", encoding="utf-8") as f:
            #     json.dump(benefits_data, f, indent=4, ensure_ascii=False)

            # Save to Redis
            key = "amex_gold_benefits"
            # self.redis_client.set(key, json.dumps(benefits_data))
            self.redis_client.set(key, "hi")

            print(f"Data stored in Redis under key: {key}")

        finally:
            with suppress(Exception):
                self.quit_driver()