# Este código fará a requisição para o API (Bored)

import requests

# mostra o caminho da url da API
url = "https://bored-api.appbrewery.com/random"

# Faz a requisição ao API e armazena a resposta em uma variável chamada 'resposta'.

resposta = requests.get(url)
try:
    dados = resposta.json()

    Atividade = dados["activity"]
    print(Atividade)
except Exception as e:
    print("Erro na requisição", e)

