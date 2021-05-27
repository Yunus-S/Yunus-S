import app
import mysql.connector

def main():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='message')
    cursor = cnx.cursor()

    query = ("SELECT * FROM message")

    cursor.execute(query,)

    liste = cursor.fetchall()
    #print(liste)

    cnx.close()

    return liste