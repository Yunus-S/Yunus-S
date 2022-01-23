import mysql.connector

def main():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='message')
    cursor = cnx.cursor()

    query = ("SELECT DATE_FORMAT(DateMessage, 'Posté le %d/%m/%y à %h:%i:%s'), Message FROM message")

    cursor.execute(query,)

    liste = cursor.fetchall()

    cnx.close()

    return liste
