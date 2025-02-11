from src.masks import get_mask_card_number, get_mask_account


if __name__ == "__main__":
    mask_number = get_mask_card_number("8888745612345879")
    mask_account = get_mask_account("15616565164884894984")
    print(mask_number)
    print(mask_account)