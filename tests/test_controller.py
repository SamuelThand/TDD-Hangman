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

    def setUp(self):
        """Creates an instance of Controller before each test."""
        self.controller_instance = Controller(GameEngine(), GUI())

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

    def test_input_callback(self):
        """The correct callback is executed when bound to the input field in the view"""
        # TODO varför blir den aldrig called?

        self.controller_instance.view.input_field = tk.Entry(self.controller_instance.view.game_frame)
        self.controller_instance.view.input_field.pack()
        callback_mock = Mock()
        self.controller_instance.view.input_field.bind("<Return>", callback_mock)
        event_mock = Mock()
        event_mock.widget = self.controller_instance.view.input_field
        event_mock.widget.insert(0, 'a')
        event_mock.widget.event_generate("<Return>")

        callback_mock.assert_called_once_with(event_mock)

    def test_input_works(self):
        """Test that the correct letter or word is passed from the input field on submit"""
        passed_input = 'a'
        self.controller_instance.view.input_field = tk.Entry(self.controller_instance.view.game_frame)
        callback_mock = Mock()
        self.controller_instance.view.input_field.bind("<Return>", callback_mock)
        event = Mock()
        event.widget = self.controller_instance.view.input_field
        event.widget.insert(0, passed_input)
        event.widget.event_generate("<Return>")

        self.assertEqual(event.widget.get(), passed_input)

    def test_displayed_word_correctly_updated:
        # TODO implement
        pass
