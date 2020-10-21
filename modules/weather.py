from requests import get

def weatherRequest(city, apikey):
    # Requisição
    response = get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}')
    data = response.json()

    # Retorno
    return f'''
Resultado:
• Nome: {data['name']},
• Clima: {data['weather'][0]['main'].replace('Clear', 'Limpo').replace('Fog', 'Névoa').replace('Mist', 'Névoa').replace('Rain', 'Chuva').replace('Clouds', 'Nuvens').replace('Drizzle', 'Chuvisco').replace('Storm', 'Tempestade')},
• Umidade: {data['main']['humidity']}%,
• Vento: {(data['wind']['speed'] * 1.6):.1f} KM/H,
• Temperatura: {(data['main']['temp'] - 273.15):.1f}°

Outras informações:
• País: {data['sys']['country']},
• Longitude {data['coord']['lon']},
• Latitude {data['coord']['lat']}'''