import os
import tkinter as tk
from tkinter import messagebox
from typing import Callable


class GUI:
    """The graphical user interface"""
    button_frame: tk.Frame
    game_frame: tk.Frame
    play_button: tk.Button
    exit_button: tk.Button
    input_field: tk.Entry or None
    image_label: tk.Label or None
    hanging_image: tk.PhotoImage or None
    word_label: tk.Label or None

    def __init__(self):
        """Initializes the GUI by setting up its components and configurations"""
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        self.root.title("Hangman")
        self.root.config(bg="grey")
        self.setup_frames()
        self.setup_buttons()
        self.input_field = None
        self.image_label = None
        self.hanging_image = None
        self.word_label = None

    def setup_frames(self):
        """Creates and packs frames"""
        self.button_frame = tk.Frame(self.root, width=800, height=100)
        self.game_frame = tk.Frame(self.root, width=800, height=400)
        self.game_frame.config(bg="black")
        self.button_frame.pack()

    def setup_buttons(self):
        """Creates and packs frames"""
        self.play_button = tk.Button(self.button_frame, text="Play", width=15, height=5)
        self.exit_button = tk.Button(self.button_frame, text="Exit", width=15, height=5)
        self.play_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.RIGHT)

    def draw_game_frame(self, word_progress: list, guesses: int):
        """
        Draw the frame for the game
        :param word_progress: The list of characters in the target word
        :param guesses: The amount of guesses made
        """
        self.game_frame.pack(fill=tk.BOTH, expand=True)
        self.setup_input_field()
        self.display_hanging_image(guesses)
        self.display_word(word_progress)

    def setup_input_field(self):
        """Displays the input field for guesses"""
        if self.input_field is None:
            self.input_field = tk.Entry(self.game_frame)
            self.input_field.pack(side=tk.BOTTOM)

    def display_hanging_image(self, guesses: int):
        """
        Displays the hanging image for the current guess count
        :param guesses: The amount of guesses made
        """
        if self.image_label is None:
            self.image_label = tk.Label(self.game_frame)
            self.image_label.pack()

        file_path = os.path.join(os.path.dirname(__file__), '..', 'other', f'{guesses}.png')
        if self.hanging_image is None or self.hanging_image['file'] != file_path:
            self.hanging_image = tk.PhotoImage(file=file_path).zoom(3)
            self.image_label.config(image=self.hanging_image)

    def display_word(self, word_progress: list):
        """
        Displays the censored target word
        :param word_progress: The list of characters in the target word
        """
        if self.word_label is None:
            self.word_label = tk.Label(self.game_frame, width=200, font=('Arial', 20))
            self.word_label.pack()

        if self.word_label['text'] != ' '.join(word_progress):
            self.word_label.config(text=' '.join(word_progress))

    def display_message(self, message: str):
        """
        Displays the passed message as a popup
        :param message: Message to display in the popup window
        """
        messagebox.showinfo('Popup', message)

    def bind_play_button(self, callback: Callable):
        """
        Bind a function to left-clicks on the play button
        :param callback: The function to execute on click
        """
        self.play_button.bind("<Button-1>", callback)
        self.root.bind("<Control-p>", callback)

    def bind_exit_button(self, callback: Callable):
        """
        Bind a function to left-clicks on the exit button
        :param callback: The function to execute on click
        """
        self.exit_button.bind("<Button-1>", callback)
        self.root.bind("<Control-q>", callback)

    def bind_input_field(self, callback: Callable):
        """
        Bind a function to submitting the input field
        :param callback: The function to execute on submission
        """
        self.input_field.bind("<Return>", callback)

    def start(self):
        """Start the GUI thread"""
        self.root.mainloop()

    def destroy(self):
        """Destroy the GUI"""
        self.root.destroy()
