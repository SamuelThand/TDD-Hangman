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
        """Tests that get_word returns a word that is nonempty/non negative"""
        game_engine = GameEngine()
        self.assertFalse(len(game_engine.get_word()) <= 0)

    def test_instance(self):
        game_engine_instance = GameEngine()
        self.assertIsInstance(game_engine_instance, GameEngine)

    def test_find_char_index(self):
        """Tests that find_char_index returns a list"""
        self.assertIsInstance(self.game_engine.find_char_index("r"), list)

    def test_find_char_index_returns_single_match(self):
        """Tests that find_char_index returns a list with a single index"""
        char = "r"
        self.game_engine.target_word = "letter"
        self.assertEqual(self.game_engine.find_char_index(char), [5])

    def test_find_char_index_returns_multiple_matches(self):
        """Tests that find_char_index returns a list with multiple indexes"""
        char = "t"
        self.game_engine.target_word = "letter"
        self.assertEqual(self.game_engine.find_char_index(char), [2, 3])

    def test_find_char_index_returns_empty_list(self):
        """Tests that find_char_index returns an empty list"""
        char = "z"
        self.game_engine.target_word = "letter"
        self.assertEqual(self.game_engine.find_char_index(char), [])
