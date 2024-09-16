import mysql.connector


class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def connect(config):
        try:
            connection = mysql.connector.connect(**config)
            print(connection)
            return connection
        except mysql.connector.Error as error:
            print(error)
            
    def close_connection(connection):
        if connection:
            connection.close()