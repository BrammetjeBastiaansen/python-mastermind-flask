from mastermind.database.models import Player, Game, db
import sqlalchemy as sa


class Player_Model:

    def __init__(self, player_service):
        self._current_player = None
        self._player_service = player_service

    @property
    def get_current_player(self):
        return self._current_player

    @get_current_player.setter
    def set_current_player(self, player):
        self._current_player = player

    def get_existing_player(self, playerName):
        return self._player_service.get_existing_player(playerName)

    def get_player_by_id(self, id):
        return self._player_service.get_player_by_id(id)

    def create_new_player(self, playerName):
        return self._player_service.create_new_player(playerName)

    def get_all_players(self):
        return self._player_service.get_all_players()

    def get_played_game_amounts_by_date(self, player_id):
        return self._player_service.get_played_game_amounts_by_date(player_id)
