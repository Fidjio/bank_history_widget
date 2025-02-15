from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card


if __name__ == "__main__":
    # mask_number = get_mask_card_number("8888745612345879")
    # mask_account = get_mask_account("15616565164884894984")
    # print(mask_number)
    # print(mask_account)
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Visa Platinum 8990922113665229"))