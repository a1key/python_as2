import requests
from bs4 import BeautifulSoup
r = requests.get('https://coinmarketcap.com/ru/currencies/bitcoin/')

html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())