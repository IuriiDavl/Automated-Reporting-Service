import pandas as pd
import requests

# Запуск локального сервера
# python -m http.server 8000 (из папки data)


response = requests.get("http://localhost:8000/db.json")
# print("Данные с локального сервера:", response.json())

rates = response.json()

rates = pd.json_normalize(rates, record_path=["rates"], meta=["date"])
rates = rates[rates["date"] == "2026-11-11"]

print(rates)

# df = pd.read_csv('transactions.csv')

# print(sum(df['currency'] != "RUB"))

# print(df)
