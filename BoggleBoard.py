class BoggleBoard(object):

    """A boggle board with a corresponding dictionary lookup trie that
    can solve itself by combining adjacent letters on the board to form valid
    words in the trie.

    Attributes:
        grid_size (int): The size of the board e.g. 3 for a 3 X 3 board
        coordinates_to_char (dict): Coordinate keys to
            corresponding character values on the grid
        trie (object): Trie of valid words to search for in the board
        adjacent_cell_map (dict): Coordinate keys to list of
            adjacent coordinates as values
        found_words (set): Valid words found in the board
    """

    def __init__(self, grid_size, coordinates_to_char, trie):
        self.grid_size = grid_size
        self.coordinates_to_char = coordinates_to_char
        self.trie = trie
        self.adjacent_cell_map = self._create_adjacent_cell_map()
        self.found_words = set()

    def _create_adjacent_cell_map(self):
        """Create a map of each cell in the grid by coordinates to its adjacent cells,
        also by coordinate.

        Returns:
            dict: Coordinate keys to list of adjacent coordinates
            Example for 2 X 2 grid:
                {
                    (0, 1): [(0, 0), (1, 0), (1, 1)],
                    (1, 0): [(0, 0), (0, 1), (1, 1)],
                    (0, 0): [(0, 1), (1, 0), (1, 1)],
                    (1, 1): [(0, 0), (0, 1), (1, 0)]
                }
        """
        adjacent_cell_map = {}
        for x_coord in range(self.grid_size):
            for y_coord in range(self.grid_size):
                adjacent_cells = self._find_adjacent_cells(x_coord, y_coord)
                adjacent_cell_map[(x_coord, y_coord)] = adjacent_cells
        return adjacent_cell_map

    def _find_adjacent_cells(self, x_coord, y_coord):
        """Find cells in grid adjacent to the cell indicated by its coordinates.

        Args:
            x_coord (int): x coordinate of cell on board
            y_coord (int): y coordinate of cell on board

        Returns:
            list: list of adjacent coordinates
            Example for coordinate (0,1):
                [(0, 0), (1, 0), (1, 1)]
        """
        adjacent_cells = []
        for x, y in [(x_coord + i, y_coord + j) for i in (-1, 0, 1)
                     for j in (-1, 0, 1) if i != 0 or j != 0]:
            if (x, y) in self.coordinates_to_char:
                adjacent_cells.append((x, y))
        return adjacent_cells

    def _create_coordinate_combos(self, coordinate_combo):
        """Create possible combinations of adjacent coordinates to feed
        into dictionary trie for valid word lookup.
        Coordinates cannot be used more than once in a combination.

        Args:
            coordinate_combo (list): list of coordinates
        """
        new_coordinate_combos = []
        for coordinate in self.adjacent_cell_map[coordinate_combo[-1]]:
            if coordinate not in coordinate_combo:
                new_coordinate_list = coordinate_combo + [coordinate]
                new_coordinate_combos.append(new_coordinate_list)
        self._check_strings(new_coordinate_combos)

    def _check_strings(self, coordinate_combos):
        """Check if the list of coordinates (converted to its string representation
        on the board) is a valid word in the dictionary lookup trie. If it is a
        valid word, add it to the board's found_words set. If the string is a
        prefix in the lookup trie, keep adding adjacent coordinates to see if a
        valid word results. If the string is not a valid prefix of any word,
        we can stop the recursion and bubble up to another option.

        Args:
            coordinate_combo (list): list of coordinates
        """
        for combo in coordinate_combos:
            string = self._convert_coordinates_to_string(combo)
            if string in self.trie:
                self.found_words.add(string)
            if len(self.trie.keys(string)) > 0:
                self._create_coordinate_combos(combo)

    def _convert_coordinates_to_string(self, coordinates):
        """Convert coordinate combination to its string representation on
        the boggle board.

        Args:
            coordinate_combo (list): list of coordinates
        Returns:
            string str: lowercase string that the coordinates represent on
            the board
        """
        string = ''
        for coordinate in coordinates:
            if coordinate in self.coordinates_to_char:
                string += self.coordinates_to_char[coordinate]
            else:
                return ''
        return string.lower()

    def find_words(self):
        """Recursively search adjacent letter combinations on the board to find
        valid words in the lookup trie.
        """
        for coordinate in self.coordinates_to_char.keys():
            self._create_coordinate_combos([coordinate])
