from bs4 import BeautifulSoup

import requests


url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text)

tr = soup.findChildren("tr")

tr = iter(tr)

next(tr)

for movie in tr:
    title = movie.find('td', {'class':'titleColumn'}).find('a').contents[0]
    print(title)
