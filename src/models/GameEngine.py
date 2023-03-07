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

    def char_validation(self, entered_input: str) -> bool:
        """
        Validates that the input is alphabetical.
        :param entered_input: char to validate
        :raises ValueError: if non-alphabetical input is provided
        :return: True if the char is alphabetical
        """
        if entered_input.isalpha():
            return True
        raise ValueError

    def word_validation(self, entered_input: str) -> bool:
        """
        Validates that the input is alphabetical and the same length as the target word.
        :param entered_input: word to validate
        :return: True if word is valid, else False
        """
        target_word_length = len(self.target_word)
        if len(entered_input) == target_word_length:
            if not entered_input.isalpha():
                raise ValueError
            return True
        return False
