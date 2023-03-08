from views.GUI import GUI
from models.GameEngine import GameEngine
from controllers.Controller import Controller


def hangman():
    """Entry point for the hangman game"""
    controller = Controller(GameEngine(), GUI())
    controller.start_gui()


if __name__ == '__main__':
    hangman()
