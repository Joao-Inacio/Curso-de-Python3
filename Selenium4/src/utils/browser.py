from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ROOT_FOLDER = Path(__file__).parent.parent.parent.parent

CHROME_DRIVER_PATH = ROOT_FOLDER / 'Selenium4' / 'bin' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    browser.get('https://google.com')
    sleep(10)
    browser.find_element(By.NAME, 'q').send_keys('Python')
    sleep(10)
    browser.find_element(By.NAME, 'btnK').click()
    sleep(20)
    browser.quit()
