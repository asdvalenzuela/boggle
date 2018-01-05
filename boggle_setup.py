from marisa_trie import Trie

"""
Methods used to read dictionary and boggle board input files,
setup trie of valid dictionary words, and codify boggle board structure.
"""


class BoggleSetupException(Exception):
    pass


def read_file(filename):
    """Open specified file and return list of lines stripped of whitespace.

    Args:
        filename (str): name of file

    Returns:
        list: list of lines stripped of whitespace
    """
    try:
        with open(filename) as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
        return lines
    except IOError:
        raise BoggleSetupException('Please enter a valid filename.')


def create_dictionary_trie(filename):
    """Remove invalid words from supplied dictionary and create trie.
    Invalid words are 2 characters or less in length.

    Args:
        filename (str): name of file to use for dictionary

    Returns:
        object: trie of valid dictionary words
    """
    words = read_file(filename)
    if not words:
        raise BoggleSetupException('A valid dictionary must be provided.')

    valid_words = []
    for word in words:
        if len(word) > 2:
            valid_words.append(word)

    return Trie(valid_words)


def process_boggle_board(filename):
    """Retrieve board size and codify board structure.

    Args:
        filename (str): name of file to use for boggle board

    Returns:
        list: [grid size (int), coordinates_to_char (dict)}
        Where grid size is the size of the board (3 for 3 X 3 grid),
            and coordinates_to_char is a dictionary of coordinate keys to
            their corresponding character value on the grid
    """
    lines = read_file(filename)
    if len(lines) < 3:
        raise BoggleSetupException(
            'A valid board of at least 2 X 2 must be provided.')

    grid_size = int(lines[0])

    grid = []
    for line in lines[2:]:
        grid.append(line.split())

    coordinates_to_char = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            coordinates_to_char[(i, j)] = grid[i][j]

    return [grid_size, coordinates_to_char]
