import json


DEFAULT_FILE_PATH = 'metadata.json'



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
