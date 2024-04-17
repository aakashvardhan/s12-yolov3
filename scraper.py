import requests
from bs4 import BeautifulSoup
import os


# Function to download an image from a URL
def download_image(image_url, folder_name, index):
    response = requests.get(image_url)
    print(response.status_code)
    if response.status_code == 200:
        with open(os.path.join(folder_name, f"image_{index}.jpg"), "wb") as file:
            file.write(response.content)


# Function to scrape images
def scrape_images(url, total_images):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("img")
    print(f"Total images found: {len(images)}")

    folder_name = "data"
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)

    image_count = 0
    for index, image in enumerate(images):
        # Assuming the image source URL is contained in the 'src' attribute
        image_url = image.get("img")
        if any(extension in image_url for extension in [".jpg", ".jpeg", ".png"]):
            download_image(image_url, folder_name, index)
            image_count += 1
            if image_count >= total_images:
                break


if __name__ == "__main__":
    # URL of the page where the images are located
    url = "https://www.istockphoto.com/photos/national-geographic-animals"

    # Number of images you want to scrape
    total_images = 100

    scrape_images(url, total_images)
