"""
Central Scrape Orchestrator
- Imports and calls all other scraper modules
"""

from celery import shared_task

# Task to be run daily by Celery
@shared_task
def run_scrapers():
    from scrapers.amex_gold import AmexGoldScraper
    from scrapers.amex_plat import AmexPlatScraper
    from scrapers.chase_saph_pref import ChaseSapphirePreferredScraper

    scrapers = {
        "amex_gold": AmexGoldScraper(),
        "amex_plat": AmexPlatScraper(),
        "chase_sapphire_preferred": ChaseSapphirePreferredScraper(),
    }

    for name, scraper_class in scrapers.items():
        print(f"Running scraper: {name}")
        scraper = scraper_class()
        scraper.scrape()

# Manual command to run script
# if __name__ == "__main__":
#     run_scrapers()