import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '301710ac412d2cfa789c329bcca394a4'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create_pokemon = {
    "name": "Aurora",
    "photo_id": 666
}

body_put_name = {
    "pokemon_id": "309925",
    "name": "Beauty",
    "photo_id": 666
}

body_add_pokeball = {
    "pokemon_id": "309925"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put_name)
print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response.text)