from app import db
from datetime import datetime


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    games = db.relationship('Game', backref='player', lazy=True)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    double_colors_allowed = db.Column(db.Boolean, nullable=False)
    color_amount = db.Column(db.Integer, nullable=False)
    position_amount = db.Column(db.Integer, nullable=False)
    played_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    answers_guessed_in_turns = db.Column(db.Integer)
    cheats_used = db.Column(db.Boolean)

    def __repr__(self):
        return f"Game(id={self.id}, player_id={self.player_id}, double_colors_allowed={self.double_colors_allowed}, color_amount={self.color_amount}, position_amount={self.position_amount}, played_on={self.played_on})"
