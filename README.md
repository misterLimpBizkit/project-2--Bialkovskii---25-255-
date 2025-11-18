# project-2--Bialkovskii---25-255-
# База данных - DB Project

Простая консольная база данных на Python с поддержкой CRUD-операций.

## Установка и запуск

```bash
# Установка пакета
pip install .

# Запуск программы
database
```

## Управление таблицами

### Создание таблицы
```bash
create_table <имя_таблицы> <столбец1:тип> <столбец2:тип> ...
```
**Пример:**
```bash
create_table users name:str age:int is_active:bool
```

### Просмотр таблиц
```bash
list_tables
```

### Удаление таблицы
```bash
drop_table <имя_таблицы>
```
**Пример:**
```bash
drop_table users
```

### Информация о таблице
```bash
info <имя_таблицы>
```
**Пример:**
```bash
info users
```

## CRUD-операции

### CREATE - Создание записи
```bash
insert into <имя_таблицы> values (<значение1>, <значение2>, ...)
```
**Пример:**
```bash
insert into users values ("Sergei", 28, true)
```
**Результат:**
```
Запись с ID=1 успешно добавлена в таблицу "users".
```

### READ - Чтение записей
```bash
# Все записи
select from <имя_таблицы>

# С условием
select from <имя_таблицы> where <столбец> = <значение>
```
**Примеры:**
```bash
select from users
select from users where age = 28
select from users where name = "Sergei" and age = 28
```
**Результат:**
```
+----+--------+-----+-----------+
| ID |  name  | age | is_active |
+----+--------+-----+-----------+
| 1  | Sergei | 28  |    True   |
+----+--------+-----+-----------+
Найдено записей: 1
```

### UPDATE - Обновление записи
```bash
update <имя_таблицы> set <столбец> = <новое_значение> where <столбец_условия> = <значение_условия>
```
**Пример:**
```bash
update users set age = 29 where name = "Sergei"
```
**Результат:**
```
Запись с ID=1 в таблице "users" успешно обновлена.
```

### DELETE - Удаление записи
```bash
delete from <имя_таблицы> where <столбец> = <значение>
```
**Пример:**
```bash
delete from users where ID = 1
```
**Результат:**
```
Запись с ID=1 успешно удалена из таблицы "users".
```

## Общие команды

### Справка
```bash
help
```

### Выход
```bash
exit
```

## Поддерживаемые типы данных

- **int** - целые числа (например: `25`, `-10`)
- **str** - строки (обязательно в кавычках: `"текст"`, `'текст'`)
- **bool** - логические значения (`true`, `false`)

## Особенности

- Автоматическая генерация поля `ID` для каждой таблицы
- Подтверждение опасных операций (удаление таблиц и данных)
- Кэширование результатов запросов для ускорения работы
- Замер времени выполнения операций
- Поддержка нескольких условий в WHERE через `and`
- Данные сохраняются в JSON-файлы в папке `data/`

## Пример сессии работы

```bash
>>> create_table users name:str age:int is_active:bool
Таблица "users" успешно создана со столбцами: ID:int, name:str, age:int, is_active:bool

>>> insert into users values ("Sergei", 28, true)
Запись с ID=1 успешно добавлена в таблицу "users".

>>> select from users where age = 28
+----+--------+-----+-----------+
| ID |  name  | age | is_active |
+----+--------+-----+-----------+
| 1  | Sergei | 28  |    True   |
+----+--------+-----+-----------+
Найдено записей: 1

>>> update users set age = 29 where name = "Sergei"
Запись с ID=1 в таблице "users" успешно обновлена.

>>> delete from users where ID = 1
Запись с ID=1 успешно удалена из таблицы "users".

>>> info users
Таблица: users
Столбцы: ID:int, name:str, age:int, is_active:bool
Количество записей: 0
```

