import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'token'
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

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create.text)

response_put_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put_name)
print(response_put_name.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)