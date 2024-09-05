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
                config = json.dump({ 'host': host, 'user': user, 'password': password, 'database': database }, file)
                #
                connection = queries.Controller(config={'host': host, 'user': user, 'password': password})
                connection.connect()
                connection.create_db(name=database)
                #
            else:
                database = input('Введите имя базы данных: ')
                config = json.dump({ 'host': host, 'user': user, 'password': password, 'database': database }, file)
                connection = queries.Controller(config=config)
                connection.connect()

    connection.close_connection()

    while True:
        command = input('\nВыход (exit)\n' +
                        '1. create_table (создать таблицу)\n' +
                        '2. add_row (добавить строку в таблицу)\n')
        if command == 'EXIT' or command == 'exit':
            break
        else:
            if command == 'create_table':
                print('create')
            elif command == 'add_row':
                print('aa')
            else:
                print('Неизвестная команда')

if __name__ == '__main__':
    main()