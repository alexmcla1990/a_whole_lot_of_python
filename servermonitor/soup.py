import requests
from bs4 import BeautifulSoup

data = requests.get('url')
soup = BeautifulSoup(data.text, 'html.parser')

data = []
for x in soup.find_all('x'):
    values = [td.text for x in x.find_all('x')]
    data.append(values)


data = []
for x in soup.find_all('x', {'class':'special'}):
    values = [td.text for x in x.find_all('x')]
    data.append(values)

data = []
div = soup.find('div', {'class': 'special_table'})
for tr in div.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    data.append(values)