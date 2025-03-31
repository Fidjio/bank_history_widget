import logging
import os

log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "masks.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)
time_format = "%Y-%m-%d %H:%M:%S"
logger = logging.getLogger("masks")
file_handler = logging.FileHandler(log_path, "w", encoding="UTF-8")
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s: %(filename)s - func: %(funcName)s. " "%(levelname)s: %(message)s", datefmt=time_format
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str | None:
    """Маскирует номер банковской карты"""
    try:
        logger.info("функция начала работу -> continue")
        if len(number_card) != 16 or not number_card.isdigit():
            logger.warning("попытка задать формат номера карты..")

            strip_number_card = number_card.replace(" ", "")

            if len(strip_number_card) != 16 or not strip_number_card.isdigit():
                logger.warning("неверный формат номера карты")
                return "Неверный номер карты!"

            logger.info("форматирование номера карты -> ok")
            logger.info("функция выполнена - ok")
            return f"{strip_number_card[:4]} {strip_number_card[4:6]}** **** {strip_number_card[-4:]}"

        logger.info("функция выполнена - ok")
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
    except Exception as ex:
        logger.critical(f"произошла ошибка: {ex}")
        return None


def get_mask_account(account_number: str) -> str | None:
    """Маскирует номер банковского счета"""
    try:
        logger.info("функция начала работу -> continue")
        if len(account_number) < 6:
            logger.warning("неверный формат номера карты")
            return "Введите корректный номер счета!"
        else:
            logger.info("функция выполнена - ok")
            return f"**{account_number[-4:]}"

    except Exception as ex:
        logger.critical(f"произошла ошибка: {ex}")
        return None
