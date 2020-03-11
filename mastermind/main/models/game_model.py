from mastermind.database.models import Game, db


class Game_Model:
    def __init__(self):
        pass

    def create_new_game(self, settings):
        print(settings)