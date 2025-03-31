from unittest.mock import patch, mock_open, MagicMock
import pandas as pd
from src.read_file_from_pandas import read_cvs_files, read_excel_files


def test_read_cvs_files(info_to_test_read_files, info_csv):

    with patch('builtins.open', mock_open(read_data=info_csv)), \
            patch('csv.DictReader') as mock_reader:
        mock_reader.return_value = info_to_test_read_files
        result = read_cvs_files('test.csv')
        assert result == info_to_test_read_files


def test_read_cvs_file_empty(info_to_test_read_files, info_csv):

    with patch('builtins.open', mock_open(read_data=info_csv)), \
            patch('csv.DictReader') as mock_reader:
        mock_reader.return_value = ""
        result = read_cvs_files('test.csv')
        assert result == []


def test_read_excel_files_success(info_to_test_read_files):
    """Тест успешного чтения Excel-файла."""

    mock_df = MagicMock()
    mock_df.to_dict.return_value = info_to_test_read_files

    with patch('pandas.read_excel', return_value=mock_df) as mock_read:
        result = read_excel_files("test.xlsx")

        # Проверяем вызовы
        mock_read.assert_called_once_with("test.xlsx")
        mock_df.to_dict.assert_called_once_with('records')

        # Проверяем результат
        assert result == info_to_test_read_files


def test_read_excel_files_file_not_found():
    """Тест обработки ошибки при отсутствии файла."""
    with patch('pandas.read_excel', side_effect=FileNotFoundError("File not found")) as mock_read:
        result = read_excel_files("none_file.xlsx")

        mock_read.assert_called_once_with("none_file.xlsx")
        assert "Ошибка: File not found" in result


def test_read_excel_files_invalid_data():
    """Тест обработки ошибки при невалидных данных."""
    with patch('pandas.read_excel', side_effect=pd.errors.EmptyDataError("No data")) as mock_read:
        result = read_excel_files("empty.xlsx")

        mock_read.assert_called_once_with("empty.xlsx")
        assert "Ошибка: No data" in result
