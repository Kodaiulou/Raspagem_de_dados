import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display
pages = 1
all = []
while True:
    url= f"https://webscraper.io/test-sites/pagination?page={pages}"
    resposta = requests.get(url)

    site = BeautifulSoup(resposta.text,"html.parser")
    cards = site.find_all("div",class_="card sitemap-card test-sites-card")
    if len(cards) == 0:
        break
    for i in range(len(cards)):
        partes = cards[i].find("h3").text.strip().split()# Pegando o H3 dentro cards
    # Separando em: Marca | Modelo | Ano |

    marca = partes[0]
    ano = partes[-1]# Pegando o ano (que é a última parte)
    modelo = f"{partes[1]} {partes[2]}"
     #PREÇO
    preco = cards[i].find("span", itemprop="price").text.strip().split()
    moeda = preco[0]
    valor = f"{preco[1]} {preco[-1]}"

    # PAÍS e Km
    paragrafos = cards[i].find_all("p", class_="card-text")
    pais = paragrafos[1].text.replace("Country of origin: ", "").strip()

    km = paragrafos[2].text.replace("Mileage: ", "").strip()
    km = km.replace(" km", "")

    # RATING
    estrelinhas = cards[i].find("div", class_="rarity-rating")["data-rating"]

    all.append({
        "Marca": marca,
        "Modelo": modelo,
        "Ano": ano,
        "Moeda": moeda,
        "Preço": valor,
        "Pais": pais,
        "Quilometragem": km,
        "Nota": estrelinhas
    })
    print(f"{marca},{ano},{modelo},{valor},{moeda},{pais},{km},{estrelinhas}")
    pages = pages + 1
df = pd.DataFrame(all)
df.to_csv("dadosCarros.csv", index=False, encoding="utf-8-sig")
display(df)
# print(resposta) #Retorna o código 200 que significa acesso executado.
# print(site) #Mostrar todo o html da página. Cuidado para não rodar dentro do laço de repetição.
