# importar librerias
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Capturamos la url ingresada en la variable "url"
url = "https://ec.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?rt=nc&LH_ItemCondition=2000%7C2010%7C2020%7C2030"
pagina = requests.get(url)

soup = BeautifulSoup(pagina.content, 'html.parser')

# nombres de los productos de ebay
productos = soup.find_all('h3', class_='s-item__title')

lista_prod = list()
count = 0
# bucle para recorrer los productos de ebay
for i in productos:
    # mostrar solo 20 productos
    if count < 20:
        lista_prod.append(i.text)
    else:
        break
    count +=1
# print(lista_prod, len(lista_prod))

############
# precio de productos de ebay
precio = soup.find_all('span', class_='s-item__price')

lista_precio = list()
count2 = 0
# bucle para recorrer los productos de ebay
for i in precio:
    # mostrar precios
    if count2 < 20:
        lista_precio.append(i.text)
    else:
        break
    count2 +=1
# print(lista_precio, len(lista_precio))

# mostrar ordenado en un dataframe con pandas
df = pd.DataFrame({'Producto:': lista_prod,'Precio:': lista_precio}, index=list(range(1,21)))
print(df)
