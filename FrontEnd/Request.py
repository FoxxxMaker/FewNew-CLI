# Este código fará a requisição para o API (Bored)

import requests

def buscar_atividade():
    # mostra o caminho da url da API
    url = "https://bored-api.appbrewery.com/random"

    # Faz a requisição ao API e armazena a resposta em uma variável chamada 'resposta'.
    resposta = requests.get(url)

    # Retorna a resposta
    dados =resposta.json()
    return dados["activity"]
    