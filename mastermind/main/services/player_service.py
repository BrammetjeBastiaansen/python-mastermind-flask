from mastermind.database.models import Game, Color, GameColor, Player, db
import sqlalchemy as sa


class Player_Service:

    @classmethod
    def get_existing_player(cls, playerName):
        return Player.query.filter_by(name=playerName).first()

    @classmethod
    def get_player_by_id(cls, id):
        return Player.query.get(id)

    @classmethod
    def get_all_players(cls):
        return Player.query.all()

    @classmethod
    def get_played_game_amounts_by_date(cls, player_id):
        return db.session.query(sa.func.date(Game.played_on).label("date"), sa.func.count(Game.id).label("amount")).filter_by(player_id=player_id).group_by(sa.func.date(Game.played_on)).all()

    @classmethod
    def create_new_player(cls, playerName):
        player = Player(name=playerName)
        db.session.add(player)
        db.session.commit()

        return player
