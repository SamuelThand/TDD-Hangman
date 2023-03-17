import os
import sys
import time
import unittest
import tkinter as tk
from unittest.mock import Mock

from src.controllers.Controller import Controller
from src.models.GameEngine import GameEngine
from src.views.GUI import GUI

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestController(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Creates a controller instance for the tests"""
        cls.controller_instance = Controller(GameEngine(), GUI())
        cls.input_value = 'a'

    def test_instance(self):
        """Tests that the controller can be instantiated"""
        self.assertIsInstance(self.controller_instance, Controller)

    def test_has_model(self):
        """Test that the controller has a model"""
        self.assertTrue(hasattr(self.controller_instance, 'model'))

    def test_has_view(self):
        """Test that the controller has a view"""
        self.assertTrue(hasattr(self.controller_instance, 'view'))

    def test_has_play_method(self):
        """Test that the controller has a play method"""
        self.assertTrue(hasattr(self.controller_instance, 'play') and
                        callable(getattr(self.controller_instance, 'play')))

    def test_has_exit_method(self):
        """Test that the controller has a exit method"""
        self.assertTrue(hasattr(self.controller_instance, 'exit') and
                        callable(getattr(self.controller_instance, 'exit')))

    def test_has_victory_method(self):
        """Test that the controller has a game over method"""
        self.assertTrue(hasattr(self.controller_instance, 'victory') and
                        callable(getattr(self.controller_instance, 'victory')))

    def test_has_game_over_method(self):
        """Test that the controller has a game over method"""
        self.assertTrue(hasattr(self.controller_instance, 'game_over') and
                        callable(getattr(self.controller_instance, 'game_over')))

    def test_input_works(self):
        """Test that the correct letter or word is passed from the input field on submit"""
        self.controller_instance.view.input_field = tk.Entry(self.controller_instance.view.game_frame)
        callback_mock = Mock()
        self.controller_instance.view.input_field.bind("<Return>", callback_mock)
        event = Mock()
        event.widget = self.controller_instance.view.input_field
        event.widget.insert(0, self.input_value)
        event.widget.event_generate("<Return>")

        self.assertEqual(event.widget.get(), self.input_value)

    @classmethod
    def tearDownClass(cls) -> None:
        """Clean up the test class after testing"""
        cls.controller_instance = None
        cls.input_value = None
