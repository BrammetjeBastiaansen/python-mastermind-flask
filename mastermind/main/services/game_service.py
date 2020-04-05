from mastermind.database.models import *
from mastermind.database.database import db_session
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

        db_session.add(game)
        db_session.commit()

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
            db_session.add(sequence_color)

        db_session.commit()
        return sequence_colors, game_colors

    def get_games_sequence(cls, game):
        return Game.query.get(game.id).game_colors

    @classmethod
    def set_pins_for_games_most_recent_attempt(cls, game, pins):
        attempt = cls.get_games_most_recent_attempt(game)

        for pin in pins:
            attempt_pin = AttemptPin(attempt_id=attempt.id, pin_id=pin.id)
            db_session.add(attempt_pin)

        db_session.commit()

    @classmethod
    def get_pin(cls, color):
        return Pin.query.filter_by(color=color).first()

    @classmethod
    def get_games_most_recent_attempt(cls, game):
        return db_session.query(Attempt).filter_by(game_id=game.id).order_by(Attempt.id.desc()).first()

    @classmethod
    def get_game_attempt_amount(cls, game):
        return db_session.query(Attempt).filter_by(game_id=game.id).count()

    @classmethod
    def get_game_attempts(cls, game):
        return db_session.query(Attempt).filter_by(game_id=game.id).all()

    @classmethod
    def create_attempt(cls, game_id, dragged_colors):
        attempt = Attempt(game_id=game_id)
        db_session.add(attempt)

        # We commit the session here so that we can use its id in the below code.
        db_session.commit()

        for color_id in dragged_colors:
            db_session.add(AttemptColor(attempt_id=attempt.id, color_id=color_id))

        db_session.commit()

        return attempt

    @classmethod
    def set_game_finished(cls, game, won):
        game = Game.query.get(game.id)
        game.is_finished = True
        game.has_won = won

        db_session.commit()