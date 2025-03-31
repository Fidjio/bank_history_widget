import os
from unittest.mock import patch

from src.external_api import convert_amount

API_KEY = os.getenv("API_KEY")


@patch("requests.request")
def test_convert_amount(mock_request, transaction_test_value_200):
    code_ru = "RUB"
    code_transaction = transaction_test_value_200["operationAmount"]["currency"]["code"]
    amount = float(transaction_test_value_200["operationAmount"]["amount"])

    mock_request.return_value.json.return_value = {"result": 200.00}

    assert convert_amount(transaction_test_value_200) == 200.00

    mock_request.assert_called()
    mock_request.assert_called_once()
    mock_request.assert_called_with(
        "GET",
        f"https://api.apilayer.com/exchangerates_data/convert?to={code_ru}&from="
        f"{code_transaction}&amount={amount}",
        headers={"apikey": API_KEY},
    )


@patch("requests.request")
def test_convert_amount_type(mock_request, transaction_test_value_200):

    mock_request.return_value.json.return_value = {"result": 200.00}
    assert type(convert_amount(transaction_test_value_200)) == float
