from mastermind.database.models import Player, db


class Player_Model:
    def __init__(self):
        self._current_player = None

    @property
    def get_current_player(self):
        return self._current_player

    @get_current_player.setter
    def set_current_player(self, player):
        self._current_player = player

    def get_existing_player(self, playerName):
        return Player.query.filter_by(name=playerName).first()

    def create_new_player(self, playerName):
        newPlayer = Player(name=playerName)
        db.session.add(newPlayer)
        return db.session.commit()