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

    def char_in_target_word(self, char: str) -> bool:
        """
        Check if a character is in the target word.
        :param char: character to check
        :return: True if the character is in the target word, False otherwise
        """
        return char in self.target_word

    def word_matches_target_word(self, word: str) -> bool:
        """
        Check if a word matches the target word.
        :param word: word to check
        :return: True if the word matches the target word, False otherwise
        """
        return word == self.target_word

