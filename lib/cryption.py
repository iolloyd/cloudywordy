from Crypto.PublicKey import RSA

import os
from os import chmod
from os.path import dirname


def get_pub_key_file():
    key_file = os.path.join(dirname(dirname(__file__)), 'keys', 'public.key')
    return key_file


def get_priv_key_file():
    key_file = os.path.join(dirname(dirname(__file__)), 'keys', 'private.key')
    return key_file


def encrypt_word(word):
    pem_file = get_pub_key_file()
    crypto = pem_file.encrypt(str(word), pem_file)
    return crypto


if __name__ == '__main__':
    key = RSA.generate(2048)
    with open(get_pub_key_file(), 'w') as f:
        chmod(get_pub_key_file(), 0600)
        f.write(key.exportKey('PEM'))

    encrypted_key = key.exportKey(pkcs=8,
                                  protection="scryptAndAES128-CBC")

    pub_key = key.publickey()
    with open(get_priv_key_file(), 'w') as f:
        f.write(pub_key.exportKey('PEM'))



