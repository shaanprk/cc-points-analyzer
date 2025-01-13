"""
Central Scrape Orchestrator
- Imports and calls all other scraper modules
"""

from celery import shared_task

# For development
from scrapers.amex_gold import AmexGoldScraper
from scrapers.amex_plat import AmexPlatScraper
from scrapers.chase_saph_pref import ChaseSaphPrefScraper
from scrapers.chase_saph_res import ChaseSaphResScraper

# For production
# from scraper.scrapers.amex_gold import AmexGoldScraper
# from scraper.scrapers.amex_plat import AmexPlatScraper
# from scraper.scrapers.chase_saph_pref import ChaseSaphPrefScraper
# from scraper.scrapers.chase_saph_res import ChaseSaphResScraper


SCRAPERS = {
    "amex_gold": AmexGoldScraper,
    "amex_plat": AmexPlatScraper,
    "chase_saph_pref": ChaseSaphPrefScraper,
    "chase_saph_res": ChaseSaphResScraper,
}

# Task to be run daily by Celery
@shared_task 
def run_scrapers():
    for name, scraper_class in SCRAPERS.items():
        print(f"Running scraper: {name}")
        scraper = scraper_class()
        scraper.scrape()
        print("-" * 40)


# Manual command to run script for testing
if __name__ == "__main__":
    run_scrapers()