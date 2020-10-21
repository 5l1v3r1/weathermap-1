from modules.banner import banner
from modules.weather import weatherRequest
from os import system

apikey = 'AQUI' # Seu token requisitado em:

def main():
	try:
		system('clear || cls')
		print(banner())

		city = input('\nCidade -> ')

		system('clear || cls')
		print(banner())

		print(weatherRequest(city, apikey))
	
	except KeyboardInterrupt:
		pass
	
	except Exception:
		print('\nERRO: A cidade informada é incorreta.')

# Função principal
main()
