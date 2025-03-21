import logging
import os
import tempfile

from src.decorators import log


def test_decorator_log_not_error(caplog):
    """ Тест для декоратора @log проверяет выводимые логи, если функция выполнена без ошибки """
    @log()
    def get_func_to_log(func, *args, **kwargs):
        return func(*args, **kwargs)

    def summ_(a, b):
        return a + b

    caplog.set_level(logging.INFO)
    get_func_to_log(summ_, 2, 4)

    assert (
        "INFO     root:decorators.py:37 Name functions: summ_ -> ok.\n"
        "INFO     root:decorators.py:38 Result functions: 6\n"
    ) in caplog.text


def test_decorator_log_with_error(caplog):
    """ Тест для декоратора @log проверяет выводимые логи, если функция выполнена с ошибкой """
    @log()
    def get_func_to_log(func, *args, **kwargs):
        return func(*args, **kwargs)

    def summ_(a, b):
        return a + b

    caplog.set_level(logging.INFO)
    get_func_to_log(summ_, 2, "4")

    assert (
        "ERROR    root:decorators.py:57 \n"
        "Function stopped.\n"
        "Name function: summ_\n"
        "Error: TypeError.\n"
        "Сообщение исключения: unsupported operand type(s) for +: 'int' and 'str'.\n"
        "Inputs: ((2, '4'), {})\n"
    ) in caplog.text


def test_decorator_log_not_error_rec_file(caplog):
    # Тестирование с временным файлом
    custom_dir = os.path.abspath("../logs")

    def summ_(a, b):
        return a + b

    with (tempfile.NamedTemporaryFile(dir=custom_dir, delete=False, mode="w") as temp_file):
        filename = temp_file.name
        # file_name_for_decorator = os.path.basename(filename)
        temp_file.close()

        @log(filename=filename)
        def get_func_to_log(func, *args, **kwargs):
            return func(*args, **kwargs)

        get_func_to_log(summ_, 2, 4)


 #        with open(filename, "r") as f:
 #            log_content = f.read()
 #            assert ('2025-03-21 23:54:05: Name functions: summ_ -> ok.\n'
 #                     '2025-03-21 23:54:05: Result functions: 6\n') == log_content


