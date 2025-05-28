from hashlib import md5
from requests import get
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%y-%m-%dH:%M:%S')
    pub_key = '0eae6ac3e9cf10f72b367618119cfe92'
    priv_key = 'c6b9e980ac8bb718ed3cf842e2bb8057f522fa97'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    def get_heroes(self):
        params = {'ts':self.timestamp, 'apikey':self.pub_key, 'hash':self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)

        data = results.json()
        print(data)
        print(data['status'])

    def get_gen1_pokemon_images(self):
        base_url = "https://raw.githubusercontent.com/PokeApi/sprites/master/sprites/pokemon/"
        return [f"{base_url}{i}.png" for i in range(1, 152)]

restmarvel = RestMarvel()
restmarvel.get_heroes()
urls = restmarvel.get_gen1_pokemon_images()

for url in urls:
    print(url)