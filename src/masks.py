# def get_mask_card_number(number_card: str) -> str:
#     """Маскирует номер банковской карты"""
#     if len(number_card) != 16 or not number_card.isdigit():
#         return "Неверный номер карты!"
#     else:
#         return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
#
#
# def get_mask_account(account_number: str) -> str:
#     """Маскирует номер банковского счета"""
#     if len(account_number) < 6:
#         return "Введите корректный номер счета!"
#     else:
#         return f"**{account_number[-4:]}"
