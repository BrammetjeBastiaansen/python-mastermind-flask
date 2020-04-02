import datetime
from mastermind.database.models import Game, db


class Game_Model:
    def __init__(self):
        self._current_game = None

    @property
    def current_game(self):
        return self._current_game

    @current_game.setter
    def current_game(self, current_game):
        self._current_game = current_game

    def create_new_game(self, player_id, double_colors_allowed, cheat_mode_allowed, amount_of_colors, amount_of_pins):
        new_game = Game(
            player_id=player_id,
            double_colors_allowed=double_colors_allowed,
            color_amount=amount_of_colors,
            position_amount=amount_of_pins,
            played_on=datetime.datetime.now(),
            cheats_used=cheat_mode_allowed,
        )

        self.current_game = new_game

        db.session.add(new_game)
        return db.session.commit()