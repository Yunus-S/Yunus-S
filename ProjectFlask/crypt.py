import nacl.secret

import app

key = b'e57fde1q5se6g8s4eq0jm48j5y2g4j8y'


def crypt_mdp(mdp):
    cryptage = nacl.secret.SecretBox(key)
    return cryptage.encrypt(bytes(mdp, 'utf-8')).hex()


def decrypt_mdp(mdpcrypt):
    decryptage = nacl.secret.SecretBox(key)
    bitconv = bytes.fromhex(mdpcrypt)
    return decryptage.decrypt(bitconv).decode('utf-8')



