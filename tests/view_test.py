import os
import sys
import unittest

from src.views.GUI import GUI

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGUI(unittest.TestCase):

    def test_instance(self):
        gui_instance = GUI()
        self.assertIsInstance(gui_instance, GUI)
