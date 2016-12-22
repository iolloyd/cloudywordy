import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

import os
from os.path import dirname


def get_pub_key_file():
    key_file = os.path.join(dirname(dirname(__file__)), 'keys', 'public.key')
    return key_file


def get_priv_key_file():
    key_file = os.path.join(dirname(dirname(__file__)), 'keys', 'private.key')
    return key_file


def encrypt_word(word):
    f = open(get_pub_key_file(), 'r')
    r = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(r)
    enc_word = cipher.encrypt(word.encode())

    return binascii.b2a_base64(enc_word)


def decrypt_word(word):
    f = open(get_priv_key_file(), 'r')
    r = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(r)
    try:
        plain_word = cipher.decrypt(word)
    except:
        plain_word = word

    return plain_word



