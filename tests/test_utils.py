import tempfile


from src.utils import get_info_transactions_json


def test_get_info_transactions_json(transaction_in_json):
    result = get_info_transactions_json("D:\\skypro\\bank_history_widget\\data\\operations.json")
    assert result[0] == transaction_in_json
    result = get_info_transactions_json("D:\\skypro\\bank_history_widget\\data\\not_file.json")
    assert result == list()

    with tempfile.NamedTemporaryFile(delete=True, mode="w") as temp_file:
        result = get_info_transactions_json(temp_file)
        assert result == list()
