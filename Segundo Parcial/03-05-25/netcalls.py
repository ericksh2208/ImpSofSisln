import requests
import shutil
import json


class Netcalls:
    def mi_primera_llamada(self):
        url = 'https://github.com'
        r = requests.get(url)
        print(r)
        print(r.content)
        print(r.status_code)


    def descargar_imagen(self, url, file_name):
        res = requests.get(url,stream= True)
        if 200==res.status_code:
            with open(file_name, 'wb')as f:
                shutil.copyfileobj(res.raw, f)
            print('imagen descargada correctamente')
        else:
            print('No se encontro la')
    def clima(self, city, apikey):
        base_url = 'https://api.openweathermap.org/data/2.5/weather?'
        params = {'q':city, 'appid':api_key, 'units': 'metric'}
        try:
            r= requests.get(base_url, params=params)
            r.raise_for_status()

            weather_data = r.json()
            if 200 == weather_data['cod']:
                print(f'El clima en {weather_data['name']}:')
                print(f'Descripcion {weather_data['weather'][0]['description']}')
                print(f'Temperatura {weather_data['main']['temp']}°C')
                print(f'Humedad {weather_data['main']['humidity']}%')
                print(f'Viento{weather_data['wind']['speed']}m/s')
            else:
                print(f'Error{weather_data['message']}')
        except:
            print('Error')

    

url = 'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcTWCjythHtwaAaQXexjvOjD8b_-UtNgI6b86f30A6aChMhUXTx6C0-AeWZQX-BbdzFDhk4X3YxNjbaS9zHk-T5ws1zBX6Xiz9lMyHbbN7Y6bfYaP4X7tVwX'
api_key = '69ec8ca2037d63a120d31c59efd0f604'
req = Netcalls()
#req.mi_primera_llamada()
#req.descargar_imagen(url, 'moto.jpg')
req.clima('Zapopan', api_key)



