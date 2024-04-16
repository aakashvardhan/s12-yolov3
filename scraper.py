import requests
from bs4 import BeautifulSoup
import os

# Function to download an image from a URL
def download_image(image_url, folder_name, image_number):
    print(f"Downloading image from {image_url}")
    response = requests.get(image_url, timeout=10)  # Adding timeout argument with a value of 10 seconds
    if response.status_code == 200:
        with open(os.path.join(folder_name, f"image_{image_number}.jpg"), "wb") as file:
            file.write(response.content)
            print(f"Image {image_number} downloaded successfully.")
    else:
        print(f"Failed to download image {image_number}. Status code: {response.status_code}")


# Main function to scrape and download images
def scrape_and_download_images(base_url, total_images):
    folder_name = "data"
    os.makedirs(folder_name, exist_ok=True)

    for i in range(total_images):
        # Generate a random image URL
        image_url = f"{base_url}/416/?random={i}"
        print(f"Downloading image {i+1}")
        download_image(image_url, folder_name, i + 1)


if __name__ == "__main__":
    base_url = "https://picsum.photos"
    total_images = 100
    scrape_and_download_images(base_url, total_images)
    print("Download completed.")
