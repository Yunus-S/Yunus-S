import mysql.connector


def recreate_database():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost')
    cursor = cnx.cursor()

    cursor.execute("DROP DATABASE message")
    cursor.execute("CREATE DATABASE message")

    cnx.close()


def recreate_tables():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database="message")
    cursor = cnx.cursor()

    cursor.execute("DROP TABLE IF EXISTS message")
    cursor.execute("DROP TABLE IF EXISTS users")

    cursor.execute("CREATE TABLE message (DateMessage DATETIME NOT NULL, Message VARCHAR(45) NOT NULL)")
    cursor.execute("CREATE TABLE users (iduser BINARY(16) NOT NULL,identifiant VARCHAR(45) NOT NULL,motdepasse VARCHAR(500) NOT NULL,email VARCHAR(100) NOT NULL,PRIMARY KEY (`iduser`))")

    cnx.close()


recreate_database()
recreate_tables()
