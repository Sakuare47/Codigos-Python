import pyshorteners 


s = pyshorteners.Shortener()

# Define o URL que você quer encurtar

url = 'https://www.exemplo.com.br'


# Encurta o URL usando o serviço TinyURL

short_url = s.tinyurl.short(url)


print(short_url)