class Game_Model:

    def __init__(self, game_service):
        self._current_game = None
        self._game_sequence = None
        self._game_service = game_service
        self._sequence = None
        self._colors = None

    @property
    def current_game(self):
        return self._current_game

    @current_game.setter
    def current_game(self, current_game):
        self._current_game = current_game

    @property
    def game_sequence(self):
        return self._sequence

    @game_sequence.setter
    def game_sequence(self, sequence):
        self._sequence = sequence

    @property
    def game_colors(self):
        return self._colors

    @game_colors.setter
    def game_colors(self, colors):
        self._colors = colors

    def create_new_game(self, player_id, double_colors_allowed, cheat_mode_allowed, amount_of_colors, position_amount):
        self.current_game = self._game_service.create_new_game(
            player_id,
            double_colors_allowed,
            cheat_mode_allowed,
            amount_of_colors,
            position_amount
        )
        self.__create_random_sequence_for_game(self.current_game, amount_of_colors, position_amount)

        return self._current_game

    def __create_random_sequence_for_game(self, game, amount_of_colors, position_amount):
        self.game_sequence, self._colors = self._game_service.create_game_sequence(game, amount_of_colors, position_amount)
