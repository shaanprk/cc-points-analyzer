"""
Base Scraper Class
- Selenium web driver set up and handles pages
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import warnings

# Suppress Deprecation Warning
warnings.filterwarnings("ignore", category=DeprecationWarning)

class BaseScraper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--headless") # Run in headless mode
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--enable-unsafe-swiftshader")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--log-level=3") # Suppress warnings and info logs from chrome
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

        self.driver = webdriver.Chrome(
            service = ChromeService(ChromeDriverManager().install()),
            options = self.options,
        )
        self.wait = WebDriverWait(self.driver, 10)

    def load_page(self, url):
        self.driver.get(url)

    def quit_driver(self):
        self.driver.quit()
        