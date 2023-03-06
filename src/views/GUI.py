import tkinter as tk
from typing import Callable


class GUI:
    """The graphical user interface"""
    button_frame: tk.Frame
    game_frame: tk.Frame
    play_button: tk.Button
    exit_button: tk.Button

    def __init__(self):
        """Initializes the GUI by setting up its components and configurations"""
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Hangman")
        self.root.config(bg="grey")
        self.setup_frames()
        self.setup_buttons()

    def setup_frames(self):
        """Creates and packs frames"""
        self.button_frame = tk.Frame(self.root, width=800, height=100)
        self.game_frame = tk.Frame(self.root, width=800, height=400)
        self.game_frame.config(bg="black")

        self.button_frame.pack()
        self.game_frame.pack()

    def setup_buttons(self):
        """Creates and packs frames"""
        self.play_button = tk.Button(self.button_frame, text="Play", width=15, height=5)
        self.exit_button = tk.Button(self.button_frame, text="Exit", width=15, height=5)
        self.play_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.RIGHT)

    def bind_play_button(self, callback: Callable):
        """Bind a function to left-clicks on the play button"""
        self.play_button.bind("<Button-1>", callback)

    def bind_exit_button(self, callback: Callable):
        """Bind a function to left-clicks on the exit button"""
        self.exit_button.bind("<Button-1>", callback)

    def start(self):
        """Start the GUI thread"""
        self.root.mainloop()

    def destroy(self):
        """Destroy the GUI"""
        self.root.destroy()
