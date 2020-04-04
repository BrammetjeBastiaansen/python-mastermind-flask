from mastermind.database.models import *
import sqlalchemy as sa

import datetime
from random import shuffle, choices, sample


class Game_Service:

    @classmethod
    def create_new_game(cls, player_id, double_colors_allowed, cheat_mode_allowed, amount_of_colors, position_amount):
        game = Game(
            player_id=player_id,
            double_colors_allowed=double_colors_allowed,
            color_amount=amount_of_colors,
            position_amount=position_amount,
            played_on=datetime.datetime.now(),
            cheats_used=cheat_mode_allowed,
        )

        db.session.add(game)
        db.session.commit()

        return game

    @classmethod
    def create_game_sequence(cls, game, amount_of_colors, position_amount):
        game_colors = Color.query.limit(amount_of_colors).all()
        color_ids = []

        for game_color in game_colors:
            color_ids.append(game_color.id)

        sequence_ids = choices(color_ids, k=position_amount) \
            if game.double_colors_allowed \
            else sample(color_ids, k=position_amount)

        sequence_colors = []

        for sequence_id in sequence_ids:
            sequence_color = GameColor(game_id=game.id, color_id=sequence_id)
            sequence_colors.append(sequence_color)
            db.session.add(sequence_color)

        db.session.commit()
        return sequence_colors, game_colors

    @classmethod
    def create_attempt(cls, game_id, dragged_colors):
        attempt = Attempt(game_id=game_id)
        db.session.add(attempt)

        # We commit the session here so that we can use its id in the below code.
        db.session.commit()

        for color_id in dragged_colors:
            db.session.add(AttemptColor(attempt_id=attempt.id, color_id=color_id))

        db.session.commit()