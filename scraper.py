import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to create a directory for saving images
def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


# Function to save images to the specified directory
def save_image(image_url, dir_name, index):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(os.path.join(dir_name, f"img_{index}.jpg"), "wb") as file:
                file.write(response.content)
    except Exception as e:
        print(f"Error - Could not download {image_url} - {e}")


# Function to scrape images
def scrape_images(search_terms, num_images, driver_path):
    # Set up the Chrome driver options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set path to chromedriver as per your configuration
    webdriver_service = webdriver.chrome.service.Service(executable_path=driver_path)

    # Choose Chrome Browser
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    for term in search_terms:
        create_directory(term)  # Create a directory for each search term
        driver.get(f"https://www.google.com/search?hl=en&tbm=isch&q={term}")

        # Scroll to the end of the page to load all images
        for _ in range(5):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(1)  # Sleep between scrolls

        # Find image elements
        images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i")
        count = 0
        for index, image in enumerate(images):
            if count >= num_images:
                break
            try:
                # Click on each image to retrieve the URL
                image.click()
                time.sleep(1)  # Sleep to allow image details to load
                large_image = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "img.n3VNCb"))
                )
                image_url = large_image.get_attribute("src")
                if image_url.startswith("http"):
                    save_image(image_url, term, index)
                    count += 1
            except Exception as e:
                print(f"Error - Could not click on {image} - {e}")

    driver.quit()


if __name__ == "__main__":

    # Define search terms and number of images
    search_terms = ["objects in house", "restaurant", "street"]
    num_images = 100
    driver_path = "data/"

    # Start scraping
    scrape_images(search_terms, num_images, driver_path)
