import requests

# GIF's URL(or any file URLs)
url = 'https://static-cse.canva.com/blob/1256154/feature_free-gifs_hero.gif'

# Downloading...
response = requests.get(url)

# If the download is successful, save the file
if response.status_code == 200:
    with open('g2.gif', 'wb') as file:
        file.write(response.content)
