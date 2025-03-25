import json
import logging
from typing import Any

time_format = "%Y-%m-%d %H:%M:%S"
logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="UTF-8")
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s: %(filename)s - func: %(funcName)s. " "%(levelname)s: %(message)s", datefmt=time_format
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_info_transactions_json(path: str) -> list[Any] | None | Any:
    """Возвращает список словарей из json-файла с данными
    о финансовых транзакциях пользователей"""
    try:
        logger.info("функция начала работу -> continue")
        with open(path, "r", encoding="utf-8") as json_f:
            logger.info(f'чтение файла "{path}"')
            info_json = json.load(json_f)

            if info_json:
                logger.info("чтение файла прошло успешно")
                return info_json

    except TypeError as ex:
        logger.critical(f"произошла ошибка: {ex}")
        return list()

    except json.decoder.JSONDecodeError:
        logger.warning("нет данных в файле")
        return list()

    except Exception as ex:
        logger.critical(f"произошла ошибка: {ex}")
        return list()
