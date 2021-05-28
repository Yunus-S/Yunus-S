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

    cursor.execute("CREATE TABLE message (sent_at VARCHAR(255), content VARCHAR(255))")
    cursor.execute("CREATE TABLE users (user_id VARCHAR(255), password VARCHAR(255), email VARCHAR(255) )")

    cnx.close()


recreate_database()
recreate_tables()
