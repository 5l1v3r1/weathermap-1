import json
import requests
import platform

from os import system

apikey = 'SUA API KEY'

syst = platform.system()

if syst == 'Linux':
	system('clear')
elif syst == 'Windows':
	system('cls')

print('-'*42)
print("""
__          __        _   _               
\ \        / /       | | | |              
 \ \  /\  / /__  __ _| |_| |__   ___ _ __ 
  \ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__|
   \  /\  /  __/ (_| | |_| | | |  __/ |   
    \/  \/ \___|\__,_|\__|_| |_|\___|_|   
    			By: BlackZacky
""")

print('-'*42)
city = input('lugar: ')

if syst == 'Linux':
	system('clear')
elif syst == 'Windows':
	system('cls')

get = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}')
tempo = json.loads(get.text)
nome = str(tempo['name'])  
clima = str(tempo['weather'][0]['main']).replace('Clear', 'Limpo').replace('Fog', 'Névoa').replace('Mist', 'Névoa').replace('Rain', 'Chuva').replace('Clouds', 'Nuvens').replace('Drizzle', 'Chuvisco').replace('Storm', 'Tempestade')
umidade = str(tempo['main']['humidity'])
longitude = str(tempo['coord']['lon'])  
latitude = str(tempo['coord']['lat'])
velocidade = str(tempo['wind']['speed'])
pais = str(tempo['sys']['country'])
temperatura = int(tempo['main']['temp']) - 273.15

print('.'*26)
print("Weather:")
print(f"• Nome: {nome}")
print(f"• Clima: {clima}")
print(f"• Umidade: {umidade}%")
print(f"• Velocidade: {velocidade} km/h")
print(f"• Temperatura: {int(temperatura)}º")
print("\nOutras informações:")
print(f"• País: {pais}")
print(f"• Longitude: {longitude}")
print(f"• Latitude: {latitude}")
print('.'*26)