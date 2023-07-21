import pyowm 



# Inicializa o OWM (OpenWeatherMap) com a sua chave de API

owm = pyowm.OWM('2447e0e1eb2e3f67a4205813935f1c2f')

# Define a cidade que você quer obter o clima

city = 'Fortaleza, CE'


# Obtém as informaçãoe sobre o clima

weather = owm.weather_at_place(city).get_weather()


# Imprime a temperatura atual em graus Celsius

temperature = weather.get_temperature('celcius')['temp']

print(f'A temperatura atual em {city} é de {temperature:.1f}°C.')