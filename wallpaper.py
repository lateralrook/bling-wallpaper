from io import BytesIO
from datetime import datetime, timedelta
import requests
import json
import os
from PIL import Image

for i in range(5, -1, -1):
    # Get the JSON data from Bing's API
    date = datetime.now() - timedelta(days=i)
    url = f'https://www.bing.com/HPImageArchive.aspx?format=js&idx={i}&n=1&mkt=en-US'
    response = requests.get(url)
    data = json.loads(response.text)

    # Extract the URL of the wallpaper
    img_url = 'https://www.bing.com' + data['images'][0]['urlbase'] + '_UHD.jpg'

    # Create the filename using the date
    filename = date.strftime('%Y-%m-%d') + '.jpg'

    # Download the image
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    img.save(filename)
