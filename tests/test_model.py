import os
import sys
import unittest

from src.models.GameEngine import GameEngine

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGameEngine(unittest.TestCase):

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
