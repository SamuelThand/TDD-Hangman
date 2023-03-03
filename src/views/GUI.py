import tkinter as tk


class GUI:
    """The graphical user interface"""

    def __init__(self):
        """Initializes the GUI by setting up its components and
        configurations"""

        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Hangman")
        self.root.config(bg="grey")
        self.setup_frames()
        self.setup_buttons()

    def setup_frames(self):
        """Creates and packs frames"""

        self.button_frame = tk.Frame(self.root, width=800, height=100)
        self.button_frame.pack()

    def setup_buttons(self):
        """Creates and packs frames"""

        play_button = tk.Button(self.button_frame, text="Play", width=15, height=5)
        exit_button = tk.Button(self.button_frame, text="Exit", width=15, height=5)

        play_button.pack(side=tk.LEFT)
        exit_button.pack(side=tk.RIGHT)

    def start(self):
        """Start the GUI thread"""

        self.root.mainloop()

    def destroy(self):
        """Destroy the GUI"""

        self.root.destroy()
