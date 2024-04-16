import requests
from bs4 import BeautifulSoup
import os

# The URL of the page you want to scrape
url = 'https://www.example.com/cifar-images'

# Make a request to the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the <img> tags on the page
img_tags = soup.find_all('img')

# Set a limit to the number of images to download
limit = 100
downloaded = 0

# Directory where you want to save the images
save_dir = 'cifar_images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Download the images
for img in img_tags:
    # Get the image source URL
    img_url = img.get('src')
    # Complete the image URL if it is incomplete
    if not img_url.startswith('http'):
        img_url = urljoin(url, img_url)
    # Get the content of the image
    img_data = requests.get(img_url).content
    # Get the basename of the image file
    filename = os.path.join(save_dir, os.path.basename(img_url))
    # Save the image file
    with open(filename, 'wb') as f:
        f.write(img_data)
    downloaded += 1
    if downloaded >= limit:
        break

print(f'Downloaded {downloaded} images to {save_dir}')