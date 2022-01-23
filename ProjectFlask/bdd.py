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



def user_signup():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='message')
    cursor = cnx.cursor()

    query = ("INSERT INTO users VALUES (UUID_TO_BIN(UUID()),%s,%s,%s)")
    mdpcrypte = crypt.crypt_mdp(app.request.form['user_password'])
    val = (app.request.form['user_id'], mdpcrypte,app.request.form['user_mail'])

    cursor.execute(query, val)

    cnx.commit()
    cnx.close()


def user_login():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='message')
    cursor = cnx.cursor()

    query = ("SELECT motdepasse FROM users WHERE identifiant = %s")
    val = (app.request.form['log_user_id'],)
    cursor.execute(query, val)

    result = cursor.fetchall()

    if not result:
        return 0
    else :
        if crypt.match_mdp(app.request.form['log_user_password'], result[0][0])==True :
            return 1
        else :
            return 0


    cnx.commit()
    cnx.close()


def user_exist_check() :
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='message')
    cursor = cnx.cursor()

    query = ("SELECT identifiant FROM users WHERE identifiant = %s")
    val = (app.request.form['user_id'],)
    cursor.execute(query, val)

    result = cursor.fetchall()
    print (result)

    if not result :
        return 1
    else :
        return 0

    cnx.commit()
    cnx.close()
