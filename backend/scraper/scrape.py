"""
Central Scrape Orchestrator
- Imports and calls all other scraper modules
"""

from celery import shared_task

from scrapers.amex_gold import AmexGoldScraper
from scrapers.amex_plat import AmexPlatScraper
from scrapers.chase_saph_pref import ChaseSapphirePreferredScraper

SCRAPERS = {
    "amex_gold": AmexGoldScraper,
    # "amex_plat": AmexPlatScraper,
    # "chase_saph_pref": ChaseSapphirePreferredScraper,
}

# Task to be run daily by Celery
@shared_task 
def run_scrapers():
    for name, scraper_class in SCRAPERS.items():
        print(f"Running scraper: {name}")
        scraper = scraper_class()
        scraper.scrape()

    print("hi")

# Manual command to run script for testing
if __name__ == "__main__":
    run_scrapers()