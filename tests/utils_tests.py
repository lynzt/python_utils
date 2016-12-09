import os
import unittest
from freezegun import freeze_time
import datetime
from utils import utils

class UtilsTests(unittest.TestCase):
    def test_soupify_html(self):
        soup = utils.soupify_html('<html><title>testing</title></html>')
        self.assertEqual(soup.title.string, 'testing')

    def test_get_current_date(self):
        with freeze_time("2012-01-14"):
            assert utils.get_current_date() == datetime.datetime(2012, 1, 14)

    def test_get_current_year(self):
        with freeze_time("2012-01-14"):
            self.assertEqual(utils.get_current_year(), 2012)

    def test_merge_dictionary_and_array_dictionary(self):
        base_dict = {'123': {'name': 'mom', 'age': 40}}
        data_to_merge = [{'id': '123', 'bio': 'the best', 'pets': 'dog'}]
        result_dict = utils.merge_dictionary_and_array_dictionary(base_dict, data_to_merge, 'id')
        element = result_dict['123']
        self.assertEqual(element['name'], 'mom')
        self.assertEqual(element['age'], 40)
        self.assertEqual(element['bio'], 'the best')

    def test_normalize_string(self):
        self.assertEqual(utils.normalize_string(u'Kendall\u00a0Powell'), 'Kendall Powell')
        self.assertEqual(utils.normalize_string(u'the company\u2019s U.S'), 'the company\'s U.S')
        self.assertEqual(utils.normalize_string(u'joint venture with Nestl\xe9'), 'joint venture with Nestle')

    def test_strip_trailing_char(self):
        self.assertEqual(utils.strip_trailing_char('', ','), '')
        self.assertEqual(utils.strip_trailing_char('abc123', ','), 'abc123')
        self.assertEqual(utils.strip_trailing_char('abc123,', ','), 'abc123')

    def get_folders_in_directory(self):
        dirs = utils.get_files_in_directory('tests/data')
        self.assertEqual(len(dirs), 3)

    def test_get_files_in_directory(self):
        files = utils.get_files_in_directory('tests/data')
        self.assertEqual(len(files), 4)

    def test_get_files_in_directory_skip_hidden(self):
        files = utils.get_files_in_directory_skip_hidden('tests/data')
        self.assertEqual(len(files), 2)

    def test_check_file_or_folder_exists(self):
        self.assertTrue(utils.check_file_or_folder_exists('tests/data/folder1'))
        self.assertFalse(utils.check_file_or_folder_exists('tests/data/folder5'))
        self.assertFalse(utils.check_file_or_folder_exists('tests/nofolder/folder1'))

    def test_check_file_exists(self):
        self.assertTrue(utils.check_file_exists('tests/data/file1.txt'))
        self.assertFalse(utils.check_file_exists('tests/data/folder1'))
        self.assertFalse(utils.check_file_exists('tests/data/file5.txt'))

    def test_move_file(self):
        path1 = 'tests/data/folder2/'
        path2 = 'tests/data/folder3/'
        utils.move_file(path1 + 'file3.txt', path2 + 'file3.txt')
        self.assertTrue(utils.check_file_exists(path2 + 'file3.txt'))
        utils.move_file(path2 + 'file3.txt', path1 + 'file3.txt')
        self.assertTrue(utils.check_file_exists(path1 + 'file3.txt'))

    def test_request_json(self):
        url = 'https://kgsearch.googleapis.com/v1/entities:search?query=GENERAL MILLS&key=%s&limit=1' % os.environ["APIKEY"]
        results = utils.request_json(url)
        self.assertEqual(results['itemListElement'][0]['@type'], 'EntitySearchResult')

# APIKEY=key_here python -m unittest discover -s tests -p "*_tests.py"
