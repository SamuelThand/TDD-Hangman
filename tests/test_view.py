import os
import sys
import unittest

from src.views.GUI import GUI

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGUI(unittest.TestCase):

    def test_instance(self):
        gui = GUI()
        self.assertIsInstance(gui, GUI)

    def test_start(self):
        self.assertTrue(hasattr(GUI, 'start') and callable(getattr(GUI, 'start')))

    def test_destroy(self):
        self.assertTrue(hasattr(GUI, 'destroy') and callable(getattr(GUI, 'destroy')))

    def test_setup_frames(self):
        self.assertTrue(hasattr(GUI, 'setup_frames') and callable(getattr(GUI, 'setup_frames')))

    def test_setup_buttons(self):
        self.assertTrue(hasattr(GUI, 'setup_buttons') and callable(getattr(GUI, 'setup_buttons')))

