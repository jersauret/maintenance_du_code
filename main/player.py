class Player():
    def __init__(self, player_name):
        self.name = player_name
        self._score_as_number = 0
        self._score_as_text = LOVE

    def score_point(Player):
        Player._score_as_number += 1
        Player.set_score_as_text(Player._score_as_number)

    def set_score_as_text(self, score_as_number):
        self._score_as_text = self.transform_number_to_text(score_as_number)
    
    def update_score_from_number(self, score_as_number):
        self._score_as_number = score_as_number
        self.set_score_as_text(score_as_number)

    def get_score_as_number(Player):
        return Player._score_as_number

    def get_score_as_text(Player):
        return Player._score_as_text

    def transform_number_to_text(score_as_number):
        if score_as_number <= 3:
            return scores_text[score_as_number]
