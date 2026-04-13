from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def scrape_prices(search_query):
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://duckduckgo.com/")

        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_bar.send_keys(search_query)
        search_bar.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "h3"))
        )

        results = driver.find_elements(By.TAG_NAME, "h3")
        print(f"\nTop Results for '{search_query}':")
        for index, result in enumerate(results[:5], 1):
            if result.text.strip():
                print(f"{index}. {result.text}")
    finally:
        driver.quit()

if __name__ == "__main__":
    query= input("what do you want to search for?")
    scrape_prices(query)
