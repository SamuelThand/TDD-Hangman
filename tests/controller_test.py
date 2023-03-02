import os
import sys
import unittest

from src.controllers.Controller import Controller

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestController(unittest.TestCase):

    def test_instance(self):
        controller_instance = Controller()
        self.assertIsInstance(controller_instance, Controller)
