from mastermind.app import db
from datetime import datetime

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    games = db.relationship('Game', back_populates='player')

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"


class GameColor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)

    game = db.relationship('Game', back_populates='game_colors')
    color = db.relationship('Color', back_populates='game_colors')

    def __repr__(self):
        return f"GameColor(id={self.id}, game_id={self.game_id}, color_id={self.color_id})"


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    double_colors_allowed = db.Column(db.Boolean, nullable=False)
    color_amount = db.Column(db.Integer, nullable=False)
    position_amount = db.Column(db.Integer, nullable=False)
    played_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    cheats_used = db.Column(db.Boolean, default=False)
    is_finished = db.Column(db.Boolean, default=False)

    player = db.relationship('Player', back_populates='games')
    game_colors = db.relationship('GameColor', back_populates='game')
    attempts = db.relationship('Attempt', back_populates='game')

    def __repr__(self):
        return f"Game(id={self.id}, player_id={self.player_id}, double_colors_allowed={self.double_colors_allowed}," \
               f" color_amount={self.color_amount}, position_amount={self.position_amount}, played_on={self.played_on}," \
               f" cheats_used={self.cheats_used})"


class AttemptColor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('attempt.id'), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)

    attempt = db.relationship('Attempt', back_populates='attempt_colors')
    color = db.relationship('Color', back_populates='attempt_colors')

    def __repr__(self):
        return f"AttemptColor(id={self.id}, attempt_id={self.attempt_id}, color_id={self.color_id})"


class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

    attempt_colors = db.relationship('AttemptColor', back_populates='attempt')
    attempt_pins = db.relationship('AttemptPin', back_populates='attempt')
    game = db.relationship('Game', back_populates='attempts')

    def __repr__(self):
        return f"Attempt(id={self.id})"


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    game_colors = db.relationship('GameColor', back_populates='color')
    attempt_colors = db.relationship('AttemptColor', back_populates='color')

    def __repr__(self):
        return f"Color(id={self.id}, name={self.name})"


class AttemptPin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('attempt.id'), nullable=False)
    pin_id = db.Column(db.Integer, db.ForeignKey('pin.id'), nullable=False)

    attempt = db.relationship('Attempt', back_populates='attempt_pins')
    pin = db.relationship('Pin', back_populates='attempt_pins')

    def __repr__(self):
        return f"AttemptPin(id={self.id}, attempt_id={self.attempt_id}, pin_id={self.pin_id})"


class Pin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(40), nullable=False)

    attempt_pins = db.relationship('AttemptPin', back_populates='pin')

    def __repr__(self):
        return f"Pin(id={self.id}, color={self.color})"
