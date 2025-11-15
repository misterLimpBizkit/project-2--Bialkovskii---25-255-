import json
import os

DATA_DIR = 'data'
DEFAULT_FILE_PATH = os.path.join(DATA_DIR, 'metadata.json')



def load_metadata(file_path=DEFAULT_FILE_PATH):

    '''
        Load metadata from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Metadata as dictionary. Returns empty dict on error.
    '''
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка, файл {file_path} не найден")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка, некорректный формат в '{file_path}'.")
        return {}
    except PermissionError:
        print(f"Нет прав на чтение файла: {file_path}")
        return {}
    
def save_metadata(metadata, file_path=DEFAULT_FILE_PATH):

    '''
       Save metadata to a JSON file.

    Args:
        file_path (str): Path to save the JSON file.
        data (dict): Data to save.

    Returns:
        None.
    '''

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(metadata, file, indent=4, ensure_ascii=False)
    except PermissionError:
        print(f"Нет прав на запись в файл: {file_path}")


def get_table_data_path(table_name):
    '''
        Get the path to the data file for a specific table.
    '''
    return os.path.join(DATA_DIR, f'{table_name}.json')

def load_table_data(table_name):
    '''
        Load data from a JSON file.

        Args:
                table_name (str): Name of the table.

        Returns:
                dict: Data as dictionary. Returns empty dict on error.
    '''
    file_path = get_table_data_path(table_name)

    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            return {}
    except FileNotFoundError:
        print(f"Ошибка, файл {file_path} не найден")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка, некорректный формат в '{file_path}'.")
        return {}
    except PermissionError:
        print(f"Нет прав на чтение файла: {file_path}")
        return {}


def save_table_data(table_name, data):
    '''
    Save data to a JSON file.

    Args:
            table_name (str): Name of the table.
            data (dict): Data to save.

    Returns:
            None.
    '''
    file_path = get_table_data_path(table_name)
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False, sort_keys=True)
    except PermissionError:
        print(f"Нет прав на запись в файл: {file_path}")
