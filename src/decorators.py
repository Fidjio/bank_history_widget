# декоратор log, который
# автоматически логирует начало и конец выполнения функции,
# а также ее результаты или возникшие ошибки.
#
# Декоратор должен принимать необязательный аргумент filename, который
# определяет, куда будут записываться логи (в файл или в консоль):
# Если filename задан, логи записываются в указанный файл.
# Если filename не задан, логи выводятся в консоль.
#
# Логирование должно включать:
# Имя функции и результат выполнения при успешной операции.
# Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
import inspect
from functools import wraps
import logging
import os

# Путь к логам
PATH_TO_LOGS = os.path.abspath("./logs/")


def log(filename = "_"):
    def log_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                if filename != "_":
                    logging.basicConfig(filename=os.path.join(PATH_TO_LOGS, filename),
                                        filemode='a',
                                        encoding="UTF-8",
                                        format="%(asctime)s: %(message)s",
                                        datefmt="%Y-%m-%d %H:%M:%S",
                                        level=logging.INFO),
                else:
                    logging.basicConfig(format="%(asctime)s: %(message)s",
                                        datefmt="%Y-%m-%d %H:%M:%S",
                                        level=logging.INFO)
                print(result)
                logging.info(f"Name functions: {args[0].__name__} -> ok.")
                logging.info(f"Result functions: {result}")

            except Exception as e:
                # Выбираем настройки вывода logging (вывод в консоль/запись в файл)
                if filename != "_":
                    logging.basicConfig(filename=os.path.join(PATH_TO_LOGS, filename),
                                        filemode='a',
                                        encoding="UTF-8",
                                        format="%(asctime)s: %(message)s",
                                        datefmt="%Y-%m-%d %H:%M:%S",
                                        level=logging.INFO)
                else:
                    logging.basicConfig(format="%(asctime)s: %(message)s",
                                        datefmt="%Y-%m-%d %H:%M:%S",
                                        level=logging.INFO)

                logging.error(f"\nFunction stopped.\n"
                             f"Name function: {(args[0].__name__)}\n"
                             f"Error: {e.__class__.__name__}.\n"
                             f"Сообщение исключения: {str(e)}.\n"
                             f"Inputs: {args[1:], kwargs}\n\n")

        return wrapper
    return log_func
