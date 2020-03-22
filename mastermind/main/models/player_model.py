from mastermind.database.models import Player, Game, db
import sqlalchemy as sa

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

    def get_player_by_id(self, id):
        return Player.query.get(id)

    def create_new_player(self, playerName):
        newPlayer = Player(name=playerName)
        db.session.add(newPlayer)
        return db.session.commit()

    def get_all_players(self):
        return Player.query.all()

    def get_played_game_amounts_by_date(self, player_id):
        return db.session.query(sa.func.date(Game.played_on).label("date"), sa.func.count(Game.id).label("amount")).filter_by(player_id=player_id).group_by(sa.func.date(Game.played_on)).all()
