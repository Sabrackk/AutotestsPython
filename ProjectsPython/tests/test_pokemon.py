import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '301710ac412d2cfa789c329bcca394a4'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '29404'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_name_my_trainer():
    response_get = requests.get(url = f'{URL}/trainers/29404')
    assert response_get.json()['trainer_name'] == 'Аврора'