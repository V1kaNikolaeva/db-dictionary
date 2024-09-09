import db
import json
import queries
# from config import config


def main():
    global config
    global connection
    try: 
        with open('config.json', 'r', encoding='utf-8') as file:
            config = json.load(file)
            connection = queries.Controller(config=config)
            connection.connect()

    except FileNotFoundError:
        with open('config.json', 'w+', encoding='utf-8') as file:
            host = input('Введите хост: ')
            user = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            create_db = input('Создать новую базу (db) или ввести существующую (ex)?\n')

            if create_db == 'DB' or create_db == 'db':
                # Create DB
                database = input('Введите имя базы данных: ')
                # В json записываем всю новую инфу
                config = json.dump({ 'host': host, 'user': user, 'password': password, 'database': database }, file)
                # В Подключение отправляем без имени БД, так как ее не существует
                connection = queries.Controller(config={'host': host, 'user': user, 'password': password})
                connection.connect()
                # Создаем БД
                connection.create_db(name=database)
                #
            else:
                database = input('Введите имя базы данных: ')
                config = json.dump({ 'host': host, 'user': user, 'password': password, 'database': database }, file)
                connection = queries.Controller(config=config)
                connection.connect()

    connection.close_connection()

    print('\nВыход (exit)\n' +
            '1. create_table (создать таблицу) column_name type length -> column_name type length... -> table_name\n' +
            '2. add_row (добавить строку в таблицу)\n')
    while True:
        command = input()
        if command == 'EXIT' or command == 'exit':
            break
        else:
            if command == 'create_table':
                print('\nПример запроса:\ncolumn_name data_type length column_name data_type length table_name\nid установится автоматически')
                table = input('Введите запрос: ')
                connection.create_table('id', 'word', 'translate', name='new_table')
                print('-> created')
            elif command == 'add_row':
                print('aa')
            else:
                print('-> Неизвестная команда')

if __name__ == '__main__':
    main()