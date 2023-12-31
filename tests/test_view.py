import os
import sys
import unittest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch

from src.views.GUI import GUI

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGUI(unittest.TestCase):
    """Tests for the GUI"""

    @classmethod
    def setUpClass(cls) -> None:
        """Creates a GameEngine instance for the tests"""
        cls.gui = GUI()

    def test_instance(self):
        """Test that the can be instantiated"""
        self.assertIsInstance(self.gui, GUI)

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

    def test_bind_play_button(self):
        """Test the play button can be bound"""
        self.assertTrue(hasattr(GUI, 'setup_buttons') and callable(getattr(GUI, 'setup_buttons')))

    def test_bind_exit_button(self):
        """Test the exit button can be bound"""
        self.assertTrue(hasattr(GUI, 'setup_buttons') and callable(getattr(GUI, 'setup_buttons')))

    def test_setup_input_field(self):
        """Test there is a method to setup the input field"""
        self.assertTrue(hasattr(GUI, 'setup_input_field') and callable(getattr(GUI, 'setup_input_field')))

    def test_draw_game_frame(self):
        """Test there is a method to draw the game frame"""
        self.assertTrue(hasattr(GUI, 'draw_game_frame') and callable(getattr(GUI, 'draw_game_frame')))

    def test_display_hanging_image(self):
        """Test there is a method to display the hanging image"""
        self.assertTrue(hasattr(GUI, 'display_hanging_image') and callable(getattr(GUI, 'display_hanging_image')))

    def test_display_word(self):
        """Test there is a method to display the word"""
        self.assertTrue(hasattr(GUI, 'display_word') and callable(getattr(GUI, 'display_word')))

    def test_display_message(self):
        """Test there is a method to display a message"""
        self.assertTrue(hasattr(GUI, 'display_message') and callable(getattr(GUI, 'display_message')))

    def test_display_message_displayed(self):
        """Test that the correct message is displayed"""
        with patch.object(messagebox, 'showinfo') as mock_showinfo:
            self.gui.display_message("Test Message")
            mock_showinfo.assert_called_once_with('Popup', 'Test Message')

    def test_word_label_instance(self):
        """Test that the word_label is not instantiated unnecessarily"""
        self.gui.display_word([])
        label_1 = self.gui.word_label
        self.gui.display_word([])
        self.assertEqual(label_1, self.gui.word_label)

    def test_setup_input_field_instance(self):
        """Tests that the input field is the child of the game frame"""
        self.gui.setup_input_field()
        self.assertIsInstance(self.gui.game_frame.winfo_children()[0], tk.Entry)

    def test_word_label_instance_label(self):
        """Tests that the word_label is a label"""
        word = ['_', '_', '_', '_', '_']
        self.gui.display_word(word)
        self.assertIsInstance(self.gui.word_label, tk.Label)

    def test_word_label_length(self):
        """The word label has the correct number of characters"""
        word = "hangman"
        self.gui.display_word(list(word))
        self.assertEqual(len(self.gui.word_label["text"]), 2 * len(word) - 1)

    def test_display_word_characteristics(self):
        """Tests that the word_label has the correct font"""
        self.gui.display_word(["_", "a", "_", "c", "d", "_", "z"])
        self.assertIsInstance(self.gui.word_label, tk.Label)
        self.assertEqual(self.gui.word_label.cget("font"), "Arial 20")

    def tearDown(self) -> None:
        self.gui.setup_frames()
        self.gui.setup_buttons()
        self.input_field = None
        self.image_label = None
        self.hanging_image = None
        self.word_label = None
