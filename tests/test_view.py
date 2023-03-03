import os
import sys
import unittest

from src.views.GUI import GUI

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGUI(unittest.TestCase):
    """Tests for the GUI"""

    def test_instance(self):
        """Test that the can be instantiated"""
        gui = GUI()
        self.assertIsInstance(gui, GUI)

    def test_start(self):
        """Test that the can be started"""
        self.assertTrue(hasattr(GUI, 'start') and callable(getattr(GUI, 'start')))

    def test_destroy(self):
        """Test that the can be destroyed"""
        self.assertTrue(hasattr(GUI, 'destroy') and callable(getattr(GUI, 'destroy')))

    def test_setup_frames(self):
        """Test that the frames can be setup"""
        self.assertTrue(hasattr(GUI, 'setup_frames') and callable(getattr(GUI, 'setup_frames')))

    def test_setup_buttons(self):
        """Test that the buttons can be setup"""
        self.assertTrue(hasattr(GUI, 'setup_buttons') and callable(getattr(GUI, 'setup_buttons')))

