import os
import sys
import unittest

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

