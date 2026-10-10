import requests
from bs4 import BeautifulSoup
import pandas as pd

pages = 1
all = []
while True:
    url= f"https://webscraper.io/test-sites/pagination?pages={pages}"
    resposta = requests.get(url)
    print(resposta)
