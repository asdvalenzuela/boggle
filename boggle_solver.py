import sys

from BoggleBoard import BoggleBoard
from boggle_setup import create_dictionary_trie
from boggle_setup import process_boggle_board

try:
    boggle_board = sys.argv[1]
    dictionary = sys.argv[2]
except IndexError:
    print 'Required args: dictionary file name, boggle board file name'
    sys.exit(1)

trie = create_dictionary_trie(dictionary)
grid_size, coordinates_to_char = process_boggle_board(boggle_board)

board = BoggleBoard(grid_size, coordinates_to_char, trie)
board.find_words()
words_found = sorted(board.found_words)

with open('solution.txt', 'w') as f:
    for word in words_found:
        f.write(word + '\n')
