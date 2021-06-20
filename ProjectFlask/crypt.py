import bcrypt

def crypt_mdp(mdp):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(mdp.encode('utf-8'), salt)
    return hashed


#fonction pour vérifier le hash des mots de passe plus tard, hashed prendra la valeur du mdp hashé dans la base de donné et mdp sera le mot de passe saisie
def match_mdp(mdpcrypt):
    hashed = None
    if bcrypt.checkpw(mdp.encode('utf-8'), hashed):
        return True
    else:
        return False



