import os
import unittest

from main.tennis_game import TennisGame


class GoldenMasterTest(unittest.TestCase):
    Dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "expectedresults")

    def set_up(self):
        self.test_cases = self.generate_test_cases()

    def tear_down(self):
        self.test_cases = None

    @staticmethod
    def generate_test_cases():
        test_cases = []
        for player1_score in range(21):
            for player2_score in range(21):
                test_cases.append(("player1", "player2", player1_score, player2_score))
                test_cases.append(("player2", "player1", player1_score, player2_score))
                test_cases.append(("", "player1", player1_score, player2_score))
                test_cases.append(("player1", "", player1_score, player2_score))
        return test_cases

   # @unittest.skip("Skipping test_record")
    def test_record(self):
        for data in self.test_cases:
            player1_name, player2_name, player1_score, player2_score = data
            try:
                game = TennisGame(player1_score, player2_score, player1_name, player2_name)
                result = self.get_current_score_display(game)
            except Exception as e:
                result = type(e).__name__ + " " + str(e)

            file_name = f"{player1_score}-{player2_score}-{player1_name}-{player2_name}.txt"
            with open(os.path.join(self.Dir, file_name), "w") as f:
                f.write(result)
    @unittest.TestCase
    def test_replay(self):
        for data in self.test_cases:
            player1_name, player2_name, player1_score, player2_score = data
            try:
                game = TennisGame(player1_score, player2_score, player1_name, player2_name)
                result = self.get_current_score_display(game)
            except Exception as e:
                result = type(e).__name__ + " " + str(e)
    
            file_name = f"{player1_score}-{player2_score}-{player1_name}-{player2_name}.txt"
            with open(os.path.join(self.Dir, file_name), "r") as f:
                expected = f.read()
    
            self.assertMultiLineEqual(expected, result)

    def get_current_score_display(self, game):
        return game.get_current_score_display()