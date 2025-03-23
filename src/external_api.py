import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_amount(transaction: Any) -> Any:
    """Принимает сумму транзакции и код валюты (например, USD) и
    возвращает сумму транзакции в рублях"""
    try:
        code_ru = "RUB"
        code_transaction = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to={code_ru}&from={code_transaction}&amount={amount}"
        )
        if code_transaction != "RUB":
            headers = {"apikey": API_KEY}
            response = requests.request("GET", url, headers=headers)
            result = response.json()
            response.raise_for_status()
            return result["result"]
        else:
            return amount

    except requests.exceptions.RequestException:
        print("An error occurred. Please try again later.")
