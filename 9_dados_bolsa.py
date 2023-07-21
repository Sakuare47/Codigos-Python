import pandas as pd
import pandas_datareader as pdr
import yfinance as yf


# Define o símbolo da ação que você quer baixar os dados

symbol = 'PETR4.SA'



# Define o intervalo de data que você quer baixar os dados

start_date = '2023-01-01'
end_date = '2023-07-18'


# Baixar os dados da ação usando o Yahoo Finance

data = pdr.get_data_yahoo(symbol, start_date, end_date)



# Imprime os dados

print(data)