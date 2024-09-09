import db


class Controller():
    def __init__(self, config: dict) -> None:
        self.config = config
        self.connection = None  
        self.cursor = None  

    def connect(self):
        self.connection = db.connect(self.config)
        self.cursor = self.connection.cursor(dictionary=True)

    def close_connection(self):
        db.close_connection(self.connection)

    def create_table(self, *args: str, name: str):
        print(*args, name)

    def create_db(self, name: str):
        self.cursor.execute(f'CREATE DATABASE {name}')

    def create_record(self, *args, table_name):
        pass

    def get_records(self, table):
        self.cursor.execute(f'SELECT * FROM {table}')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


