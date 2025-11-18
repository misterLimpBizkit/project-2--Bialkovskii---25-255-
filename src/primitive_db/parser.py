def parser_insert_command(insert_args):
    '''
    Parse the insert command arguments.

    Args:
        insert_args (list): The arguments of the insert command.

    Returns:
        list: The table name and the values to insert.
    '''
    if insert_args[0].lower() != 'into':
        print('Ожидается ключевое слово "into".')
        return None, None
    
    if len(insert_args) < 4:
        print('Использование: insert into <table> values (<value1>, <value2>, ...)')
        return None, None
    
    
    table_name = insert_args[1]

    if insert_args[2].lower() != 'values':
        print('Ожидается ключевое слово "values".')
        return None, None
    
    values = []
    for arg in insert_args[3:]:
        cleaned_arg = arg.strip('() ')
        if cleaned_arg:
            values.append(cleaned_arg)

    return table_name, values

def parse_value(value_str):
    '''
    Converts a string value to the correct Python type.
    
    Args:
        value_str (str): String value
        
    Returns:
        Any type: int, bool, str or None in case of error
    '''
    if not value_str:
        return None
        
    value_str = value_str.strip()
    
    if value_str.isdigit():
        return int(value_str)

    if value_str.lower() in ('true', 'false'):
        return value_str.lower() == 'true'
    
    return str(value_str)

def parse_where_clause(where_args):
    '''
    Parse the where command arguments.

    Args:
        where_args (list): The arguments of the insert command.

    Returns:
        dict: The dictionary of where arguments.
    '''
    if not where_args:
        return None
    
    where_clause = {}
    i = 0

    while i < len(where_args):
        if i + 2 >= len(where_args):
            print('Некорректное условие where: недостаточно аргументов.')
            return None
        
        column = where_args[i]
        operator = where_args[i + 1]
        value_str = where_args[i + 2]

        if operator != '=':
            print(f'Оператор {operator} не поддерживается. Используйте "=".')
            return None
        
        value = parse_value(value_str)
        if value is None:
            return None
        
        where_clause[column] = value
        
        i += 3

        if i < len(where_args):
            if where_args[i].lower() == 'and':
                i += 1
                continue
            else:
                print(f"Ожидается 'and', получено {where_args[i]}.")
                return None
        
    return where_clause
    
def parse_select_command(select_args):
    '''
    Parse the SELECT command arguments.

    Args:
        select_args (list): The arguments of the Select command.

    Returns:
        list: list of commands or None
    '''
    if len(select_args) < 2:
        print('Использование: select from <table> [where <condition>]')
        return None, None
    
    if select_args[0].lower() != 'from':
        print('Ожидается ключевое слово "from"')
        return None, None
    
    table_name = select_args[1]
    where_clause = None

    if len(select_args) > 2 and select_args[2].lower() == 'where':
        where_clause = parse_where_clause(select_args[3:])
        print(where_clause)
        if where_clause is None:
            print('Нет условия.')
            return None, None
        
    return table_name, where_clause
