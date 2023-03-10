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

    def bind_menu_buttons(self):
        """Bind the menu buttons with controller defined callbacks"""
        self.view.bind_play_button(self.play)
        self.view.bind_exit_button(self.exit)

    def bind_input_field(self):
        self.view.bind_input_field(self.submit_input)

    def play(self, event: Event):
        """Play the game"""
        self.model.start_game()
        self.view.draw_game_frame(self.model.word_progress, self.model.guesses)
        self.bind_input_field()

    def exit(self, event: Event):
        """Exit the application"""
        self.view.destroy()
        sys.exit(1)

    def submit_input(self, event: Event):
        """Submit input to the model"""
        self.view.display_word(self.model.make_guess(event.widget.get()))
        self.view.display_hanging_image(self.model.guesses)

        if self.model.victory():
            # TODO implement victory notification and game reset
            print('victory')
        elif self.model.game_over():
            # TODO implement game over notification and game reset
            print('game_over')

    def start_gui(self):
        """Start the GUI"""
        self.view.start()
