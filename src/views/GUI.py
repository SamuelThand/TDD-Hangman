import tkinter as tk
from typing import Callable


class GUI:
    """The graphical user interface"""
    button_frame: tk.Frame
    game_frame: tk.Frame
    play_button: tk.Button
    exit_button: tk.Button
    input_field: tk.Entry
    image_label: tk.Label or None
    hanging_image: tk.PhotoImage or None
    word_label: tk.Label or None

    def __init__(self):
        """Initializes the GUI by setting up its components and configurations"""
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Hangman")
        self.root.config(bg="grey")
        self.setup_frames()
        self.setup_buttons()
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
        """Draw the frame for the game"""
        self.game_frame.pack(fill=tk.BOTH, expand=True)
        self.setup_input_field()
        self.display_hanging_image(guesses)
        self.display_word(word_progress)

    def setup_input_field(self):
        """Displays the input field for guesses"""
        self.input_field = tk.Entry(self.game_frame)
        self.input_field.pack(side=tk.BOTTOM)

    def display_hanging_image(self, guesses: int):
        """Displays the hanging image for the amount of guesses"""
        if self.image_label is not None:
            self.image_label.destroy()
            self.image_label = None
            self.image_label = None

        self.hanging_image = tk.PhotoImage(file=f'../src/other/{guesses}.png').zoom(3)
        self.image_label = tk.Label(self.game_frame, image=self.hanging_image)
        self.image_label.pack()

    def display_word(self, word: list):
        """Displays the censored target word"""
        if self.word_label is not None:
            self.word_label.destroy()
            self.word_label = None

        self.word_label = tk.Label(self.game_frame, text=' '.join(word),
                                   width=200, font=('Arial', 20))
        self.word_label.pack()

    def bind_play_button(self, callback: Callable):
        """Bind a function to left-clicks on the play button"""
        self.play_button.bind("<Button-1>", callback)

    def bind_exit_button(self, callback: Callable):
        """Bind a function to left-clicks on the exit button"""
        self.exit_button.bind("<Button-1>", callback)

    def bind_input_field(self, callback: Callable):
        """Bind a function to submitting the input field"""
        self.input_field.bind("<Return>", callback)

    def start(self):
        """Start the GUI thread"""
        self.root.mainloop()

    def destroy(self):
        """Destroy the GUI"""
        self.root.destroy()
