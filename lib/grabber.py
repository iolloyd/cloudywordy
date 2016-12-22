# import nltk
# nltk.download()
import sys
from collections import Counter
from lib.cloudsql import save_frequencies

reload(sys)
sys.setdefaultencoding('utf8')

import re
from bs4 import BeautifulSoup
from tornado.httpclient import HTTPClient as Client, HTTPError


def save_top_words(url):
    data = fetch_from_url(url)
    words = good_words(data)
    frequency_map = get_word_frequencies(words)
    save_frequencies(frequency_map)


def fetch_from_url(url):
    client = Client()
    try:
        html = client.fetch(url)
        body = unicode(html.body)
        soup = BeautifulSoup(body, "html.parser")
        data = soup.findAll(text=True)
        return data
    except HTTPError as e:
        print('Received a non-200 response: {}'.format(e))
    except Exception as e:
        print("Error: {}".format(e))

    client.close()


def good_words(data):
    sentences = [w for w in data if good_words_filter(w)]
    words = [s.split() for s in sentences]
    words = [w for sub in words for w in sub]

    return words


def good_words_filter(soup_node):
    not_tag = lambda x: x.parent.name not in ['[document]', 'head', 'script', 'style']
    not_comment = lambda x: not re.match('<!--.*-->', str(x))
    not_empty = lambda x: x not in ['', '\n', ]

    # Want to use nltk but had some issues downloading the corpora

    return not_tag(soup_node) and \
           not_comment(soup_node) and \
           not_empty(soup_node)


def get_word_frequencies(words, most_wanted=100):
    counter = Counter()
    for word in words:
        counter[word] += 1

    return counter.most_common(most_wanted)


def nouns_and_verbs_only(words):
    # s = nltk.word_tokenize(words)
    pass


