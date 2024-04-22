import requests
import os


API_KEY = '43436962-2f637a7010cb24edd3bd62fc2'
SEARCH_TERM = 'tiger photography'
TOTAL_IMAGES = 100
URL = f'https://pixabay.com/api/?key={API_KEY}&q={SEARCH_TERM}&image_type=photo&per_page={TOTAL_IMAGES}'

response = requests.get(URL)
data = response.json()

# Create a directory to save the images
if not os.path.exists('data'):
    os.makedirs('data')

for i, hit in enumerate(data['hits'], start=1):
    image_url = hit['largeImageURL']
    image_response = requests.get(image_url)
    
    # Save the image
    with open(f'data/image_{i}.jpg', 'wb') as file:
        file.write(image_response.content)
    
    print(f'Downloaded image {i} of {TOTAL_IMAGES}')

print('Download completed.')