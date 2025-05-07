import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'token'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '29404'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_name_my_trainer1():
    response_get1 = requests.get(url = f'{URL}/trainers/29404')
    assert response_get1.json()['trainer_name'] == 'Аврора'

def test_name_my_trainer2():
    response_get2 = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get2.json()['data'][0]['trainer_name'] == 'Аврора'