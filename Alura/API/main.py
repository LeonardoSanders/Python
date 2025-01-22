from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível no mundo da programação!
    '''
    return {'Hello':'World!'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes!
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante,'Cardapio': dados_restaurante}
    else:
        return {'ERRO': f'{response.status_code} - {response.text}'}
    
    '''
    Para executar e acessar os dados do FastAPI é preciso rodar o seguinte comando no terminal:
    uvicorn main:app --reload

    PS: main refere-se ao nome do arquido que contem o codigo!

    Para acessar a Query (valor do restaurante) é preciso digitar no endpoint do navegador:
    ?restaurante=NomeDoRestaurante
    '''