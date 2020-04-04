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
    def set_pins_for_games_most_recent_attempt(cls, game, pins):
        attempt = cls.get_games_most_recent_attempt(game)

        for pin in pins:
            attempt_pin = AttemptPin(attempt_id=attempt.id, pin_id=pin.id)
            db.session.add(attempt_pin)

        db.session.commit()


    @classmethod
    def get_pin(cls, name):
        return Pin.query.filter_by(name=name).first()

    @classmethod
    def get_games_most_recent_attempt(cls, game):
        return db.session.query(Attempt).filter_by(game_id=game.id).order_by(Attempt.id.desc()).first()

    @classmethod
    def get_game_attempt_amount(cls, game):
        return db.session.query(Attempt).filter_by(game_id=game.id).count()
