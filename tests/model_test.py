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