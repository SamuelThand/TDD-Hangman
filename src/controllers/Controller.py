import sys

from tkinter import Event, END
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

    def play(self, _: Event):
        """Play the game"""
        self.view.play_button.config(state='disabled')
        self.view.play_button.unbind('<Button-1>')
        self.model.start_game()
        self.view.draw_game_frame(self.model.word_progress, self.model.guesses)
        self.bind_input_field()
        self.view.input_field.config(state="normal")
        self.view.input_field.focus_set()

    def exit(self, _: Event):
        """Exit the application"""
        self.view.destroy()
        sys.exit(1)

    def submit_input(self, event: Event):
        """Submit input to the model"""
        try:
            self.view.display_word(self.model.make_guess(event.widget.get()))
            event.widget.delete(0, END)
            self.view.display_hanging_image(self.model.guesses)
        except ValueError as e:
            # TODO implement incorrect input type notification
            message = str(e)
            # print(message)
            self.view.display_message(message)
        except Exception as e:
            # TODO show exception message in notification
            message = str(e)
            # print(message)
            self.view.display_message(message)

        if self.model.victory():
            self.view.play_button.config(state='normal')
            self.view.bind_play_button(self.play)
            self.view.input_field.config(state="readonly")
            self.view.input_field.unbind('<Return>')
            self.view.display_message('Victory!')

        elif self.model.game_over():
            self.view.play_button.config(state='normal')
            self.view.bind_play_button(self.play)
            self.view.input_field.config(state="readonly")
            self.view.input_field.unbind('<Return>')
            self.view.display_word(list(self.model.target_word))
            self.view.display_message('Game Over!')

    def start_gui(self):
        """Start the GUI"""
        self.view.start()
