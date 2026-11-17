import argparse
import sys
import pandas as pd
from pathlib import Path
import requests

def api():
    # Запуск локального сервера
    # python -m http.server 8000 (из папки data)

    response = requests.get("http://localhost:8000/db.json")
    # print("Данные с локального сервера:", response.json())

    rates = response.json()

    rates = pd.json_normalize(rates, record_path=["rates"], meta=["date"])
    rates = rates[rates["date"] == "2026-11-11"]

    return rates

def main():
    parser = argparse.ArgumentParser(
        description="Скрипт для обработки файла транзакций за указанную дату"
    )
    parser.add_argument(
        "file_path", type=Path, help="Путь к CSV файлу"
    )
    parser.add_argument(
        "date", type=str, help="Дата в формате ГГГГ-ММ-ДД"
    )

    args = parser.parse_args()

    
    if not args.file_path.exists():
        print(f"Ошибка: файл {args.file_path} не найден.")
        sys.exit(1)


    print(f"Читаем файл: {args.file_path}")
    print(f"Фильтруем по дате: {args.date}")

    df = pd.read_csv(args.file_path)

    print(f"В файле {len(df)} строк, ниже первые 5.")
    print(df.head(5))


if __name__ == "__main__":
    main()
