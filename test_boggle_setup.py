import unittest

from mock import patch

import boggle_setup
from boggle_setup import BoggleSetupException
from boggle_setup import create_dictionary_trie
from boggle_setup import process_boggle_board
from boggle_setup import read_file


class BoggleSetupTest(unittest.TestCase):

    def test_read_file_returns_list_of_lines(self):
        lines = read_file('dictionary.txt')

        self.assertEqual(lines[0], 'aa')
        self.assertEqual(len(lines), 267751)

    def test_read_file_with_invalid_filename_throws_exception(self):
        with self.assertRaises(BoggleSetupException):
            read_file('fake_file_name')

    def test_create_dictionary_trie_returns_trie(self):
        with patch.object(boggle_setup, 'read_file') as mock_read_file:
            mock_read_file.return_value = ['ap', 'app', 'apple',
                                           'pe', 'peach', 'pear']

            trie = create_dictionary_trie('fake_file_name')

            self.assertTrue('app' in trie)
            self.assertFalse('pe' in trie)

    def test_create_dictionary_trie_with_no_words_throws_exception(self):
        with patch.object(boggle_setup, 'read_file') as mock_read_file:
            mock_read_file.return_value = []

            with self.assertRaises(BoggleSetupException):
                create_dictionary_trie('fake_file_name')

    def test_process_boggle_board_returns_grid_size_and_coordinate_map(self):
        with patch.object(boggle_setup, 'read_file') as mock_read_file:
            mock_read_file.return_value = ['2', '', 'T E', 'A M']

            grid_size, coordinates_to_char = process_boggle_board(
                                                        'fake_file_name')

            self.assertEqual(grid_size, 2)
            self.assertEqual(coordinates_to_char[(0, 0)], 'T')
            self.assertEqual(coordinates_to_char[(0, 1)], 'E')
            self.assertEqual(coordinates_to_char[(1, 0)], 'A')
            self.assertEqual(coordinates_to_char[(1, 1)], 'M')

    def test_process_boggle_board_with_no_lines_throws_exception(self):
        with patch.object(boggle_setup, 'read_file') as mock_read_file:
            mock_read_file.return_value = []

            with self.assertRaises(BoggleSetupException):
                process_boggle_board('fake_file_name')
