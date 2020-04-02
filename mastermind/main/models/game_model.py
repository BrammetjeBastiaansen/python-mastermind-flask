import datetime

from mastermind.database.models import Game, Color, GameColor, db
from random import shuffle, choices


class Game_Model:
    def __init__(self):
        db.create_all()
        self._current_game = None

    @property
    def current_game(self):
        return self._current_game

    @current_game.setter
    def current_game(self, current_game):
        self._current_game = current_game

    def create_new_game(self, player_id, double_colors_allowed, cheat_mode_allowed, amount_of_colors, position_amount):
        new_game = Game(
            player_id=player_id,
            double_colors_allowed=double_colors_allowed,
            color_amount=amount_of_colors,
            position_amount=position_amount,
            played_on=datetime.datetime.now(),
            cheats_used=cheat_mode_allowed,
        )

        self.current_game = new_game

        db.session.add(new_game)

        result = db.session.commit()

        self.__create_random_sequence_for_game(new_game.id, amount_of_colors, position_amount)

        return result


    def __create_random_sequence_for_game(self, game_id, amount_of_colors, position_amount):
        game_colors = Color.query.limit(amount_of_colors).all()
        color_ids = []

        for game_color in game_colors:
            color_ids.append(game_color.id)

        sequence_ids = choices(color_ids, k=position_amount)

        for sequence_id in sequence_ids:
            sequence_color = GameColor(game_id=game_id, color_id=sequence_id)
            db.session.add(sequence_color)

        db.session.commit()
