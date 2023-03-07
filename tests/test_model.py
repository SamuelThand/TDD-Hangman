import os
import sys
import unittest

from src.models.GameEngine import GameEngine

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGameEngine(unittest.TestCase):

    def setUp(self):
        """ Creates an instance of GameEngine before each test. """
        self.game_engine = GameEngine()

    def test_get_word_returns_word(self):
        """Tests that get_word returns a string"""
        game_engine = GameEngine()
        self.assertIsInstance(game_engine.get_word(), str)

    def test_get_word_length_nonempty_non_negative(self):
        """Tests that get_word returns a word that is nonempty/non-negative"""
        game_engine = GameEngine()
        self.assertFalse(len(game_engine.get_word()) <= 0)

    def test_instance(self):
        game_engine_instance = GameEngine()
        self.assertIsInstance(game_engine_instance, GameEngine)

    def test_char_in_target_word(self):
        """Tests that char_in_target_word returns a boolean"""
        result = self.game_engine.char_in_target_word("a")
        self.assertIsInstance(result, bool, "char_in_target_word should return a boolean")

    def test_char_in_target_word_correct(self):
        """Tests that char_in_target_word returns True if the character is in the target word"""
        self.game_engine.target_word = "test"
        result = self.game_engine.char_in_target_word("t")
        self.assertTrue(result, "char_in_target_word should return True if the character is in the target word")

    def test_char_in_target_word_incorrect(self):
        """Tests that char_in_target_word returns False if the character is not in the target word"""
        self.game_engine.target_word = "test"
        result = self.game_engine.char_in_target_word("w")
        self.assertFalse(result or result is None,
                         "char_in_target_word should return False if the character is not in the target word")

    def test_word_matches_target_word(self):
        """Tests that word_matches_target_word returns a boolean"""
        result = self.game_engine.word_matches_target_word("test")
        self.assertIsInstance(result, bool, "word_matches_target_word should return a boolean")

    def test_word_matches_target_word_correct(self):
        """Tests that word_matches_target_word returns True if the word matches the target word"""
        self.game_engine.target_word = "test"
        result = self.game_engine.word_matches_target_word("test")
        self.assertTrue(result, "word_matches_target_word should return True if the word matches the target word")

    def test_word_matches_target_word_incorrect(self):
        """Tests that word_matches_target_word returns False if the word does not match the target word"""
        self.game_engine.target_word = "test"
        result = self.game_engine.word_matches_target_word("west")
        self.assertFalse(result or result is None,
                         "word_matches_target_word should return False if the word does not match the target word")
