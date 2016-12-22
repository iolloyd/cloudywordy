import rsa
import os
from os.path import dirname


def get_key(key_type):
    if key_type not in ['priv', 'pub']:
        raise AttributeError("You provided a type that I don't know. "
                             "You have to provide either 'priv' or 'pub'")

    key_file = os.path.join(dirname(dirname(__file__)), 'keys', '{}.pem'.format(key_type))
    with open(key_file, 'r') as f:
        pub = f.read()
    return pub


def encrypt_word(word):
    return word
    pub = get_key('pub')
    crypto = rsa.encrypt(word, pub)
    return crypto


