import json
import unidecode
import requests
import datetime
import time
import os
from bs4 import BeautifulSoup

def request_html(url):
    r = requests.get(url)
    return r.text

def request_json(url):
    r = requests.get(url)
    return r.json

def soupify_html(html):
    return BeautifulSoup(html, "html5lib")

def get_current_date():
    return datetime.datetime.now()

def get_current_year():
    return (get_current_date()).year

def normalize_string(u_str):
    u_str = _unidecode_string(u_str)
    return u_str

def _unidecode_string(u_str):
    return unidecode.unidecode(u_str)

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
    print json.dumps(json_str, indent=4, separators=(',', ': '))

def wait_n_seconds(seconds=1):
    print "waiting %s seconds" % (seconds)
    time.sleep(seconds) # sleep for passed number of seconds else default to 1 second


# def convert_name_to_websafe(string):
#     string = string.lower()
#     string = re.sub('[\s\.,\&\(\)']', '-', string)
#     return string;


def get_files_in_directory_skip_hidden(path):
    dirs = get_files_in_directory(path)
    return filter(lambda f: not f.startswith('.'), dirs) # remove files names starting w/ dot

def get_files_in_directory(path):
    return next(os.walk(path))[2]

def get_folders_in_directory(path):
    return next(os.walk(path))[1]

def check_file_or_folder_exists(path):
    return os.path.exists(path)

def move_file(from_path, to_path):
    os.rename(from_path, to_path)
    # return os.path.exists(path)

def check_file_exists(path):
    return os.path.isfile(path)
