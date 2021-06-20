import app
import mysql.connector
import datetime
import crypt


def main():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='message')
    cursor = cnx.cursor()

    query = ("INSERT INTO message VALUES (%s,%s)")
    val = (datetime.datetime.now(), app.request.form['message'])

    cursor.execute(query, val)


    cnx.commit()
    cnx.close()




def user():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='message')
    cursor = cnx.cursor()

    query = ("INSERT INTO users VALUES (%s,%s,%s)")
    mdpcrypte = crypt.crypt_mdp(app.request.form['user_password'])
    print(mdpcrypte)

    
    val = (app.request.form['user_id'], mdpcrypte,app.request.form['user_mail'])

    cursor.execute(query, val)


    cnx.commit()
    cnx.close()


