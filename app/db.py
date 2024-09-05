import mysql.connector


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