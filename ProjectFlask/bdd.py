import self as self
import nacl.secret
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
    val = (time(), app.request.form['message'])

    cursor.execute(query, val)


    cnx.commit()
    cnx.close()


def time ():
    tps = datetime.datetime.now()
    temps = str(tps.year) + '/' + str(tps.month) + '/' + str(tps.day)

    return temps


def user():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='message')
    cursor = cnx.cursor()

    query = ("INSERT INTO users VALUES (%s,%s,%s,%s)")
    mdpcrypte = crypt.crypt_mdp(app.request.form['user_password'])
    print(mdpcrypte)
    #mdp = crypt.decrypt_mdp(mdpcrypte)
    #print(mdp)
    val = (None,app.request.form['user_id'], mdpcrypte,app.request.form['user_mail'])

    cursor.execute(query, val)


    cnx.commit()
    cnx.close()


