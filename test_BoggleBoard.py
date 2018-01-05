import unittest

from BoggleBoard import BoggleBoard
from boggle_setup import create_dictionary_trie


class BoggleBoardTest(unittest.TestCase):

    def setUp(self):
        coordinates_to_char = {
            (0, 0): 'T',
            (0, 1): 'E',
            (1, 0): 'A',
            (1, 1): 'M'
        }
        trie = create_dictionary_trie('dictionary.txt')
        self.board = BoggleBoard(3, coordinates_to_char, trie)

    def test_create_adjacent_cell_map(self):
        adjacent_cell_map = self.board._create_adjacent_cell_map()

        self.assertEqual(adjacent_cell_map[(0, 0)], [(0, 1), (1, 0), (1, 1)])
        self.assertEqual(adjacent_cell_map[(1, 0)], [(0, 0), (0, 1), (1, 1)])

    def test_find_adjacent_cells_small_grid(self):
        adjacent_cells = self.board._find_adjacent_cells(0, 1)

        self.assertEqual(adjacent_cells, [(0, 0), (1, 0), (1, 1)])

    def test_convert_coordinates_to_string(self):
        converted_string = self.board._convert_coordinates_to_string([
            (0, 0), (0, 1), (1, 0)])

        self.assertEqual(converted_string, 'tea')

    def test_convert_coordinates_to_string_coordinates_not_in_grid(self):
        converted_string = self.board._convert_coordinates_to_string([
            (0, 0), (0, 1), (2, 0)])

        self.assertEqual(converted_string, '')

    def test_find_words_finds_all_matches(self):
        self.board.find_words()

        found_words = sorted(self.board.found_words)
        self.assertEqual(len(found_words), 14)
        self.assertEqual(found_words, ['ate', 'eat', 'eta',
                                       'mae', 'mat', 'mate',
                                       'meat', 'met', 'meta',
                                       'tae', 'tam', 'tame',
                                       'tea', 'team'])
