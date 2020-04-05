from sqlalchemy import *
from sqlalchemy.orm import relationship
from mastermind.database.database import Base
from datetime import datetime


class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)

    games = relationship('Game', back_populates='player')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"


class GameColor(Base):
    __tablename__ = 'game_color'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'), nullable=False)
    color_id = Column(Integer, ForeignKey('color.id'), nullable=False)

    game = relationship('Game', back_populates='game_colors')
    color = relationship('Color', back_populates='game_colors')

    def __init__(self, game_id=None, color_id=None):
        self.game_id = game_id
        self.color_id = color_id

    def __repr__(self):
        return f"GameColor(id={self.id}, game_id={self.game_id}, color_id={self.color_id})"


class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    double_colors_allowed = Column(Boolean, nullable=False)
    color_amount = Column(Integer, nullable=False)
    position_amount = Column(Integer, nullable=False)
    played_on = Column(DateTime, nullable=False, default=datetime.utcnow)
    cheats_used = Column(Boolean, default=False)
    is_finished = Column(Boolean, default=False)
    has_won = Column(Boolean, default=False)

    player = relationship('Player', back_populates='games')
    game_colors = relationship('GameColor', back_populates='game')
    attempts = relationship('Attempt', back_populates='game')

    def __init__(self, player_id=None, double_colors_allowed=None, color_amount=None, position_amount=None, played_on=datetime.utcnow, cheats_used=False, is_finished=False, has_won=False):
        self.player_id = player_id
        self.double_colors_allowed = double_colors_allowed
        self.color_amount = color_amount
        self.position_amount = position_amount
        self.played_on = played_on
        self.cheats_used = cheats_used
        self.is_finished = is_finished
        self.has_won = has_won

    def __repr__(self):
        return f"Game(id={self.id}, player_id={self.player_id}, double_colors_allowed={self.double_colors_allowed}," \
               f" color_amount={self.color_amount}, position_amount={self.position_amount}, played_on={self.played_on}," \
               f" cheats_used={self.cheats_used})"


class AttemptColor(Base):
    __tablename__ = 'attempt_color'
    id = Column(Integer, primary_key=True)
    attempt_id = Column(Integer, ForeignKey('attempt.id'), nullable=False)
    color_id = Column(Integer, ForeignKey('color.id'), nullable=False)

    attempt = relationship('Attempt', back_populates='attempt_colors')
    color = relationship('Color', back_populates='attempt_colors')

    def __init__(self, attempt_id=None, color_id=None):
        self.attempt_id = attempt_id
        self.color_id = color_id

    def __repr__(self):
        return f"AttemptColor(id={self.id}, attempt_id={self.attempt_id}, color_id={self.color_id})"


class Attempt(Base):
    __tablename__ = 'attempt'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'), nullable=False)

    attempt_colors = relationship('AttemptColor', back_populates='attempt')
    attempt_pins = relationship('AttemptPin', back_populates='attempt')
    game = relationship('Game', back_populates='attempts')

    def __init__(self, game_id=None,):
        self.game_id = game_id

    def __repr__(self):
        return f"Attempt(id={self.id})"


class Color(Base):
    __tablename__ = 'color'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)

    game_colors = relationship('GameColor', back_populates='color')
    attempt_colors = relationship('AttemptColor', back_populates='color')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"Color(id={self.id}, name={self.name})"


class AttemptPin(Base):
    __tablename__ = 'attempt_pin'
    id = Column(Integer, primary_key=True)
    attempt_id = Column(Integer, ForeignKey('attempt.id'), nullable=False)
    pin_id = Column(Integer, ForeignKey('pin.id'), nullable=False)

    attempt = relationship('Attempt', back_populates='attempt_pins')
    pin = relationship('Pin', back_populates='attempt_pins')

    def __init__(self, attempt_id=None, pin_id=None):
        self.attempt_id = attempt_id
        self.pin_id = pin_id

    def __repr__(self):
        return f"AttemptPin(id={self.id}, attempt_id={self.attempt_id}, pin_id={self.pin_id})"


class Pin(Base):
    __tablename__ = 'pin'
    id = Column(Integer, primary_key=True)
    color = Column(String(40), nullable=False)

    attempt_pins = relationship('AttemptPin', back_populates='pin')

    def __init__(self, color=None):
        self.color = color

    def __repr__(self):
        return f"Pin(id={self.id}, color={self.color})"
