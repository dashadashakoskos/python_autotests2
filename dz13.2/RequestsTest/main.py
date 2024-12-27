import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2fc8e2b5adafb4861457d0799f08726b'
HEADER = {'Contrnt-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Заврбульба",
    "photo_id": 777
}

body_change = {
    "pokemon_id": "172138",
    "name": "Заврбульба",
    "photo_id": 111
}

body_catch = {
    "pokemon_id": "172138"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch )
print(response_catch.text)
