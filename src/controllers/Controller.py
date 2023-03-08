import sys

from tkinter import Event
from src.models.GameEngine import GameEngine
from src.views.GUI import GUI


class Controller:
    """The controller of the application"""
    model: GameEngine
    view: GUI

    def __init__(self, model: GameEngine, view: GUI):
        """Initializes the model and view, and binds the
        main functional buttons"""
        self.model = model
        self.view = view
        self.bind_menu_buttons()

    def play(self, event: Event):
        """Play the game"""
        print('Play')

    def exit(self, event: Event):
        """Exit the application"""
        self.view.destroy()
        sys.exit(1)

    def bind_menu_buttons(self):
        """Bind the menu buttons with controller defined callbacks"""
        self.view.bind_play_button(self.play)
        self.view.bind_exit_button(self.exit)

    def start_gui(self):
        """Start the GUI"""
        self.view.start()
