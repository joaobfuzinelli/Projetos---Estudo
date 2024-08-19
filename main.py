import requests


link = f"https://brasilapi.com.br/api/cnpj/v1/{48373126000138}"

def search():
    buscador = requests.get(link)
    convert = buscador.json()
    print(convert)
    

test = search()
