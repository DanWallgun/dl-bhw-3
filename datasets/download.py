from bs4 import BeautifulSoup
import requests

image_idx = 0

for page_idx in range(1, 11):
    r = requests.get(f'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page={page_idx}')
    soup = BeautifulSoup(r.content, "lxml")
    links = [
        img['src']
        for img in soup.find_all('img', attrs={'height': 209, 'width': 140})
    ]
    for link in links:
        image_bytes = requests.get(link).content
        with open(f'imdb/{image_idx}.jpg', 'wb') as f:
            f.write(image_bytes)
        image_idx += 1