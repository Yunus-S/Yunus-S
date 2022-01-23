from flask import Flask
from flask import abort, redirect, url_for, render_template
from flask import request
import bdd
import printMessage
from flask import session


# https://flask.palletsprojects.com/en/1.1.x/quickstart/


app = Flask(__name__)
app.secret_key = '_5#ax2L"FaQ4z\n\xec]/'

# Page d'accueil du site.
# Par exemple : http://127.0.0.1:5000/
@app.route('/home')
def home():
    # On ne fait rien de spécial, on va juste retourner le contenu html du template home.html
    # Voir templates/home.html

    if 'username' in session:
        historique = printMessage.main()
        return render_template('home.html', message=historique, len = len(historique))
    else :
        return redirect(url_for('index'))



@app.route('/add_message', methods=['POST'])
def add_message():
    # On affiche dans la console le message écrit par l'utilisateur

    print(request.form['message'])

    # TODO extraire le message et l'enregistrer en base de données
    bdd.main()

    # Une fois le traitement terminé, on redirige vers la page d'accueil
    return redirect(url_for('home'))


@app.route('/signup')
def signup():
    if 'username' in session:
        return redirect(url_for('index'))
    else :
        return render_template('signup.html')


@app.route('/new_acc', methods=['POST'])
def newacc():
    print(request.form['user_id'])
    print(request.form['user_mail'])
    print('check')
    exist_check = bdd.user_exist_check()
    print('check2')
    print(exist_check)
    if exist_check == 1 :
        bdd.user_signup()
        return redirect(url_for('login'))
    else :
        return redirect(url_for('signup'))


@app.route('/login')
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    else :
        return render_template('login.html')


@app.route('/user_login', methods=['GET','POST'])
def user_login():
    log = bdd.user_login()
    if log == 1 :
        session['username'] = request.form['log_user_id']
        return redirect(url_for('index'))
    else :
        return redirect(url_for('login'))


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Connecté en tant que ' + username + '<br>' + "<b><a href = '/logout'>Deconnection</a></b>" '<br>' "<a href = '/home'>Zone de texte</a>"
    return "Vous n'êtes pas connecté. <br><a href = '/login'>" + "Cliquez ici pour vous connecter</a><br><a href = '/signup'>" + "ou ici pour créer un compte</a>"


@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
