#!/usr/bin/python3

import numpy as np
np.seterr(all='ignore')

"""
This file contains all Abstract GameBoard classes but no actual finished Implementations.
The Finished Implementations can be cound in the file gameboards.py
"""


class GameBoard:
    """[Abstract] The base class for a Gameboard"""

    # Board Dimensions
    ROWS = 7
    COLS = 6

    # Occupation Constants
    RED = 0
    YELLOW = 1
    EMPTY = 2

    # Occupation Strings
    STRINGS = {
        EMPTY: " ",
        YELLOW: "O",
        RED: "X"
    }

    def __init__(self):
        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.set_occupation(r, c, self.EMPTY)

    def copy_gamestate(self, other):
        """Copies gamestate of other gameboard"""
        if not isinstance(other, GameBoard):  # Check if both of them are Gameboards
            raise ValueError("Can't copy gamestate of a non-gameboard.".format(type(self), type(other)))
        if self.ROWS != other.ROWS or self.COLS != other.COLS:
            raise ValueError("Dimensions mismatch.")

        for r in range(self.ROWS):
            for c in range(self.COLS):
                occupation = other.get_occupation(r, c)
                self.set_occupation(r, c, occupation)

    def clone(self):
        """Returns an identical instance to itself"""
        out = self.__class__()
        out.copy_gamestate(self)
        return out

    def set_occupation(self, row, col, player):
        """Sets The field at row, col to a specific value"""
        raise NotImplementedError("Please Implement this method")

    def get_occupation(self, row, col):
        """Gets the field value at row, col"""
        raise NotImplementedError("Please Implement this method")

    def has_won(self, player):
        """Determines if a given player has won or not"""
        raise NotImplementedError("Please Implement this method")

    def is_full(self):
        """Checks wether the game board is full"""
        raise NotImplementedError("Please Implement this method")

    def is_finished(self):
        """Checks if the game has finished"""
        return self.is_full() or self.has_won(self.RED) or self.has_won(self.YELLOW)

    def is_legal(self, row):
        """Checks wether any player can play in this row"""
        raise NotImplementedError("Please Implement this method")

    def place_stone(self, row, player):
        """Place a stone into a column and let it drop to the bottom.
        Returns True iff Action was successfull"""
        raise NotImplementedError("Please Implement this method")

    def count3(self, player):
        """Counts how many times a player has 3 in a row"""
        raise NotImplementedError("Please Implement this method")

    @classmethod
    def get_occupation_string(cls, occupation):
        if occupation in cls.STRINGS:
            return cls.STRINGS[occupation]
        else:
            raise ValueError("Invalid Game Board occupation: {}".format(occupation))

    @classmethod
    def other_player(cls, player):
        if player == cls.RED:
            return cls.YELLOW
        elif player == cls.YELLOW:
            return cls.RED
        else:
            raise ValueError("Unknown Player: {}".format(player))

    def __str__(self):
        """Returns a string representation of the game board"""
        lines = []
        for c in range(self.COLS - 1, -1, -1):
            occupations = []
            for r in range(self.ROWS):
                occupation = self.get_occupation(r, c)
                occupation_string = self.get_occupation_string(occupation)
                occupations.append(occupation_string)
            lines.append("|".join(occupations))
        lines.append("-" * (2 * self.ROWS - 1))
        numbers = []
        for n in range(self.ROWS):
            numbers.append(str(n))
        lines.append("|".join(numbers))
        return "\n".join(lines)

    def __eq__(self, other):
        """Checks wether two GameBoards are equal"""
        if not isinstance(other, GameBoard):  # Check if both of them are Gameboards
            raise ValueError("Can't compare {} and {}.".format(type(self), type(other)))
        else:
            if self.ROWS != other.ROWS or self.COLS != other.COLS:  # Check if dimensions match
                return False

            # Check if all other fields are equal
            for r in range(self.ROWS):
                for c in range(other.ROWS):
                    if self.get_occupation(r, c) != other.get_occupation(r, c):
                        return False
            return True
