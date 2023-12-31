import json
import os
from random import randrange


class GameEngine:
    """
    The GameEngine class is responsible for the logic of the game.
    """
    target_word: str
    word_progress: list
    guessed_characters: list
    max_guesses: int = 8
    guesses: int

    def __init__(self):
        """Initialize the game engine"""
        self.target_word = ""
        self.word_progress = []
        self.guessed_characters = []
        self.guesses = 0

    def start_game(self):
        """Start the game"""
        self.target_word = self.get_word()
        self.generate_word_list()
        self.guesses = 0
        self.guessed_characters = []

    def generate_word_list(self):
        """Generate the word to be displayed to the player"""
        self.word_progress = ['_' for _ in self.target_word]

    def game_over(self) -> bool:
        """
        Test if it is game over
        :return It is game over
        """
        return self.guesses == self.max_guesses

    def victory(self):
        """Test if the victory condition is true"""
        return self.target_word == ''.join(self.word_progress)

    def get_word(self) -> str:
        """
        Get a random word from other/words.json
        :return A random word
        """
        try:
            file_path = os.path.join(os.path.dirname(__file__), '..', 'other', 'words.json')
            with open(file_path) as file_handle:
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
        if len(entered_input) < 1:
            raise ValueError("Empty input is not accepted")
        if entered_input.isalpha():
            if entered_input in self.guessed_characters:
                raise Exception("Letter already in guessed letters")
            return True
        raise ValueError("Invalid guess, numbers and symbols are not accepted")

    def word_validation(self, entered_input: str) -> bool:
        """
        Validates that the input is alphabetical and the same length as the target word.
        :param entered_input: word to validate
        :return: True if word is valid, else False
        """
        target_word_length = len(self.target_word)
        if len(entered_input) == target_word_length:
            if not entered_input.isalpha():
                raise ValueError("Invalid guess, numbers and symbols are not accepted")
            return True
        raise Exception("Guess is not the same length as target word")

    def store_guessed_char(self, char: str, indexes: [int]) -> None:
        """
        Stores the given character in the lists for guessed characters and word progress.
        :param char: char to store
        :param indexes: list of indexes for letter word progress
        """
        self.guessed_characters.append(char)
        for index in indexes:
            self.word_progress[index] = char

    def make_guess(self, guess: str) -> [str]:
        """
        Make a char or word guess against the target word.
        The game progression is updated according to the result including:
        - guesses counter
        - word progress
        :param guess: word or char to guess
        :return: current version of word progress list
        :raises Exception: If a letter already in guessed characters is passed
        """
        index: [int] = []
        guess = str.lower(guess)
        if len(guess) <= 1:
            self.char_validation(guess)
            if self.char_in_target_word(guess):
                index = self.find_char_index(guess)
            else:
                self.guesses += 1
            self.store_guessed_char(guess, index)
        else:
            self.word_validation(guess)
            if self.word_matches_target_word(guess):
                for index, char in enumerate(guess):
                    self.word_progress[index] = char
            else:
                self.guesses = self.max_guesses
        return self.word_progress
