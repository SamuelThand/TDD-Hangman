import json
from random import randrange


class GameEngine:
    """
    The GameEngine class is responsible for the logic of the game.
    """

    def __init__(self):
        self.target_word = ""

    def get_word(self) -> str:
        """Get a random word from other/words.json"""
        try:
            with open('../src/other/words.json') as file_handle:
                words = json.load(file_handle)
                return words[f'{randrange(len(words) - 1)}']
        except IOError as e:
            print(f'Error opening file: {e}')

    def find_char_index(self, char: str) -> list:
        """
        Find one or multiple indexes of a character in the target word
        :param char: character to find
        :return: list of indexes
        """
        matches = []
        for index, letter in enumerate(self.target_word):
            if letter == char:
                matches.append(index)
        return matches
