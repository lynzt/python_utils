import json
import unidecode
import requests
import random
import datetime
import time
import os
import urllib
from slugify import Slugify
from bs4 import BeautifulSoup

def request_html(url):
    r = requests.get(url)
    return r.text

def request_json(url):
    r = requests.get(url)
    return json.loads(r.text)

def soupify_html(html, type):
    if type == 'lxml':
        return BeautifulSoup(html, 'lxml')
    elif type == 'html5lib':
        return BeautifulSoup(html, 'html5lib')

def get_and_soupify(url, type):
    html = request_html(url)
    return soupify_html(html, type)

def encode_uri_string(str):
    return urllib.parse.quote_plus(str)

def parse_url_string(str):
    return urllib.parse.urlparse(str)

def get_base_url(scheme, netloc):
    return scheme + '://' +netloc

def get_current_date():
    return datetime.datetime.now()

def get_current_year():
    return (get_current_date()).year

def normalize_string(u_str):
    return unidecode.unidecode(u_str)

def _is_string(x):
    return isinstance(x, str)

# merge data into main dict...
def merge_dictionary_and_array_dictionary(base_dict, array_dict_data_to_merge, base_dict_key):
    for data in array_dict_data_to_merge:
        key = data[base_dict_key]
        base_dict = _merge_new_data(base_dict, data, base_dict_key, key)
    return base_dict

def _merge_new_data(base_dict, data, base_dict_key, key):
    for key_to_add in data:
        if key_to_add != base_dict_key:
            base_dict[key][key_to_add] = data[key_to_add]
    return base_dict

def strip_trailing_char(str, char):
    return str.rstrip(char)

def json_pretty_print(json_str):
    print (json.dumps(json_str, indent=4, separators=(',', ': ')))

def get_fist_char(string):
    return string[0]

def wait_n_seconds(seconds=1, msg=''):
    print ('wait %s seconds || %s' % (seconds, msg))
    time.sleep(seconds) # sleep for passed number of seconds else default to 1 second

def get_random_nbr_between(nbr1, nbr2):
    return random.randint(nbr1, nbr2)

def slugify_string(str):
    my_slugify = Slugify()
    my_slugify.pretranslate = {'AT&T':'att'}
    my_slugify.to_lower=True
    return my_slugify(str)

    # return slugify(str, pretranslate={'AT&T':'att'}, to_lower=True)
