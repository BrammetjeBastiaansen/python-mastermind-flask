from mastermind.app import db
from datetime import datetime

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    games = db.relationship('Game', backref='player', lazy=True)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"


# TODO: As soon as the database session is commited, all the duplicate colors in game_colors will not be saved. I.e. a game can't have duplicate colors. The id column doesn't really do anything.
game_colors = db.Table("game_colors",
    db.Column("id", db.Integer),
    db.Column("game_id", db.Integer, db.ForeignKey("game.id")),
    db.Column("color_id", db.Integer, db.ForeignKey("color.id")),
    db.PrimaryKeyConstraint("id"),
)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    double_colors_allowed = db.Column(db.Boolean, nullable=False)
    color_amount = db.Column(db.Integer, nullable=False)
    position_amount = db.Column(db.Integer, nullable=False)
    played_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    cheats_used = db.Column(db.Boolean, default=False)
    answers_guessed_in_turns = db.Column(db.Integer, default=0)
    colors = db.relationship("Color", secondary=game_colors, backref="game", lazy=True)
    attempts = db.relationship('Attempt', backref='game', lazy=True)

    def __repr__(self):
        return f"Game(id={self.id}, player_id={self.player_id}, double_colors_allowed={self.double_colors_allowed}," \
               f" color_amount={self.color_amount}, position_amount={self.position_amount}, played_on={self.played_on}," \
               f" cheats_used={self.cheats_used})"


# TODO: Read todo above.
attempt_colors = db.Table("attempt_colors",
    db.Column("id", db.Integer),
    db.Column("attempt_id", db.Integer, db.ForeignKey("attempt.id")),
    db.Column("color_id", db.Integer, db.ForeignKey("color.id")),
    db.PrimaryKeyConstraint("id"),
)


class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    colors = db.relationship("Color", secondary=attempt_colors, backref="attempt", lazy=True)

    def __repr__(self):
        return f"Attempt(id={self.id})"


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable = False)

    def __repr__(self):
        return f"Color(id={self.id}, name={self.name})"
