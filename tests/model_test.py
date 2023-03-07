import os
import sys
import unittest

from src.models.GameEngine import GameEngine

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGameEngine(unittest.TestCase):

    def setUp(self):
        """ Creates an instance of GameEngine before each test. """
        self.game_engine = GameEngine()

    def test_instance(self):
        game_engine_instance = GameEngine()
        self.assertIsInstance(game_engine_instance, GameEngine)

    def test_char_validation_positive(self):
        """ Valid single-character input should return true. """
        value = "a"

        result = self.game_engine.char_validation(value)

        self.assertTrue(result, "a should be a valid input.")

    def test_char_validation_negative(self):
        """ Invalid single-character input should throw ValueError"""
        value = "3"

        self.assertRaises(ValueError, self.game_engine.char_validation, value)

    def test_word_validation_positive(self):
        """ Valid words with the same length as target_word returns true """
        guess_word = "test"
        self.game_engine.target_word = guess_word

        result = self.game_engine.word_validation(guess_word)

        self.assertTrue(result,
                        f"{guess_word} should be valid because it is same length as {self.game_engine.target_word}.")

    def test_number_word_validation_negative(self):
        """ Invalid words including numbers throws ValueError """
        number_word = "tes2"
        target_word = "test"
        self.game_engine.target_word = target_word

        self.assertRaises(ValueError, self.game_engine.char_validation, number_word)

    def test_short_word_validation_negative(self):
        """ Invalid words of the wrong length returns false """
        short_word = "tes"
        target_word = "test"
        self.game_engine.target_word = target_word

        result = self.game_engine.word_validation(short_word)

        self.assertFalse(result, f"{short_word} should be invalid because it is shorter than {target_word}.")