from random import shuffle;

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

    def create_attempt(self, dragged_colors):
        return self._game_service.create_attempt(self._current_game.id, dragged_colors)

    def __create_random_sequence_for_game(self, game, amount_of_colors, position_amount):
        self.game_sequence, self._colors = self._game_service.create_game_sequence(game, amount_of_colors, position_amount)

    def set_pins_and_check_win(self):
        has_won = True

        # Get all pins
        black_pin = self._game_service.get_pin("Black")
        white_pin = self._game_service.get_pin("White")
        no_pin = self._game_service.get_pin("None")

        # Get all attempt and sequence color ids
        attempt_color_ids = [attempt_color.color.id for attempt_color in self._game_service.get_games_most_recent_attempt(self._current_game)]
        sequence_color_ids = [game_color.color.id for game_color in self._game_sequence.game_colors]
        
        pins = []

        # Check for black pins
        i = 0
        while i < len(attempt_color_ids):
            if attempt_color_ids[i] == sequence_color_ids[i]:
                del attempt_color_ids[i]
                del sequence_color_ids[i]
                pins.append(black_pin)
            else:
                has_won = False
                i += 1

        # Check for white pins
        while i < len(attempt_color_ids):
            if attempt_color_ids[i] in sequence_color_ids:
                del attempt_color_ids[i]
                del sequence_color_ids[i]
                pins.append(white_pin)
            else:
                i += 1

        # Check for no pins
        for _ in range(len(attempt_color_ids)):
            pins.append(no_pin)

        # Randomize the pins list
        shuffle(pins)

        self._game_service.set_pins_for_games_most_recent_attempt(self.current_game, pins)

        # If the user has not played 12 attempts yet without winning, return true.
        # If 12 attempts have already been made, return the has_won boolean
        # Also return all pins
        return None if not has_won and self._game_service.get_game_attempt_amount(self._current_game) < 12 else has_won, pins


    def __set_pins_for_attempt_and_check_win(self, attempt, pins):
        return self._game_service.set_pins_for_attempt_and_check_win(attempt, pins)
