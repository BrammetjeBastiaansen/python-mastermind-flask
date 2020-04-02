from mastermind.main.services.game_service import Game_Service


class Game_Model:

    def __init__(self, game_service):
        self._current_game = None
        self._game_sequence = None
        self._game_service = game_service

    @property
    def current_game(self):
        return self._current_game

    @current_game.setter
    def current_game(self, current_game):
        self._current_game = current_game

    def create_new_game(self, player_id, double_colors_allowed, cheat_mode_allowed, amount_of_colors, position_amount):
        self.current_game = self._game_service.create_new_game(
            player_id,
            double_colors_allowed,
            cheat_mode_allowed,
            amount_of_colors,
            position_amount
        )
        self.__create_random_sequence_for_game(self.current_game.id, amount_of_colors, position_amount)

        return self._current_game

    def __create_random_sequence_for_game(self, game_id, amount_of_colors, position_amount):
        self._game_service.create_game_sequence(game_id, amount_of_colors, position_amount)

    def get_game_sequence(self):
        return self._game_service.get_game_colors(self._current_game)
