import views.GUI as GUI


def hangman():
    """Entry point for the hangman game"""

    gui = GUI.GUI()
    gui.start()


if __name__ == '__main__':
    hangman()
