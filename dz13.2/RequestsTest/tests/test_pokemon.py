import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2fc8e2b5adafb4861457d0799f08726b'
HEADER = {'Contrnt-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '12525'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get_name = requests.get(url = f'{URL}/me', headers = HEADER)
    assert response_get_name.json()["data"][0]["trainer_name"] == 'ДашаКос'