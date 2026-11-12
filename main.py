import argparse
import sys
import pandas as pd
from pathlib import Path

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
