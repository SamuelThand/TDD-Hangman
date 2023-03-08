from src.models.GameEngine import GameEngine
from src.views.GUI import GUI


class Controller:
    """The controller of the application"""
    model: GameEngine
    view: GUI

    def __init__(self, model, view):
        self.model = model
        self.view = view


