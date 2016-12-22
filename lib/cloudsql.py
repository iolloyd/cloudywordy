import hashlib
import os
import pymysql.cursors
from cryption import encrypt_word


CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')


def connect_to_cloudsql():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD)

    else:
        db = pymysql.connect(host='127.0.0.1',
                             user=CLOUDSQL_USER,
                             passwd=CLOUDSQL_PASSWORD)

    return db


def get_data_from_cloudsql():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('SHOW VARIABLES')
    words = [r for r in cursor.fetchall()]

    return words


def save_frequencies(frequency_map):
    values = ["('{0}', '{1}', {2})".format(hashed(x), encrypt_word(x), y)
              for x, y in frequency_map]

    values_string = ",".join(values)
    sql = """
        INSERT INTO words (hashed_word, encrypted_word, total_frequency)
        VALUES {0}
        ON DUPLICATE KEY UPDATE total_frequency=total_frequency+VALUES(total_frequency)
        """.format(values_string)
    print(sql)
    db = connect_to_cloudsql()
    with db.cursor() as cursor:
        cursor.execute(sql)



def hashed(word):
    super_secret_hash = 'wewantlloyd'
    hashed_word = hashlib.sha256(word + super_secret_hash).hexdigest()

    return hashed_word
