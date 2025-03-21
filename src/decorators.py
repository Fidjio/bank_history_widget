import logging
import os
from functools import wraps
from typing import Any, Callable

# Путь к логам
PATH_TO_LOGS = os.path.abspath("./logs/")


def log(filename: str = "") -> Callable[..., Any]:
    """Декоратор, который выводит логи декорируемой функции в консоль
    или записывает их в файл. Декоратор принимает необязательный аргумент filename - имя файла,
    в который будут записаны логи. Если имя файла не указано, логи будут выведены в консоль."""

    def log_func(func: Callable[..., Any]) -> Callable[..., Any]:
        """Описание выше"""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            """Функция выполняет функцию и обрабатывает ее исключения,
            и логирует результат (ошибка или успешное выполнение функции)"""
            try:
                result = func(*args, **kwargs)
                if filename != "":
                    logging.basicConfig(
                        filename=os.path.join(PATH_TO_LOGS, filename),
                        filemode="w",
                        encoding="UTF-8",
                        format="%(asctime)s: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                    )
                else:
                    logging.basicConfig(
                        format="%(asctime)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO
                    )
                logging.info(f"Name functions: {args[0].__name__} -> ok.")
                logging.info(f"Result functions: {result}")
                logging.shutdown()

            except Exception as e:
                # Выбираем настройки вывода logging (вывод в консоль/запись в файл)
                if filename != "":
                    logging.basicConfig(
                        filename=os.path.join(PATH_TO_LOGS, filename),
                        filemode="w",
                        encoding="UTF-8",
                        format="%(asctime)s: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO,
                    )
                else:
                    logging.basicConfig(
                        format="%(asctime)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO
                    )

                logging.error(
                    f"\nFunction stopped.\n"
                    f"Name function: {(args[0].__name__)}\n"
                    f"Error: {e.__class__.__name__}.\n"
                    f"Сообщение исключения: {str(e)}.\n"
                    f"Inputs: {args[1:], kwargs}\n\n"
                )
                logging.shutdown()

        return wrapper

    return log_func
