import requests
from bs4 import BeautifulSoup
import pandas as pd
pages = 1
all = []
while True:
    url= f"https://webscraper.io/test-sites/pagination?pages={pages}"
    resposta = requests.get(url)

    site = BeautifulSoup(resposta.text,"html.parser")
    cards = site.find_all("div",class_="card sitemap-card test-sites-card")

# print(resposta) #Retorna o código 200 que significa acesso executado.
# print(site) #Mostrar todo o html da página. Cuidado para não rodar dentro do laço de repetição.
