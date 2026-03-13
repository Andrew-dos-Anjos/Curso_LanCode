# A104
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com/'

site = requests.get(url)
if site.status_code == 200:
    soup = bs(site.text, 'html.parser') # (textos do site, 'estruturaHTML.analise')
    frases = soup.find_all('span', attrs={'class': 'text'}) # Dentro da tag span, buscar pelos atributos de texto em class.
    for frase in frases:
        print(frase.text)


url = 'https://books.toscrape.com/'

site = requests.get(url)
if site.status_code == 200:
    soup = bs(site.text, 'html.parser')
