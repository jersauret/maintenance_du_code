import os
import unittest

from main.tennis1 import TennisGame1 as TennisGame


class GoldenMasterTest(unittest.TestCase):
    Dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "expectedresults")

    def setUp(self):
        self.test_cases = self.generate_test_cases()

    def tearDown(self):
        self.test_cases = None

    @staticmethod
    def generate_test_cases():
        test_cases = []
        for score_player1 in range(21):
            for score_player2 in range(21):
                test_cases.append(("player1", "player2", score_player1, score_player2))
                test_cases.append(("player2", "player1", score_player1, score_player2))
                test_cases.append(("", "player1", score_player1, score_player2))
                test_cases.append(("player1", "", score_player1, score_player2))
        return test_cases

    @unittest.skip("Skip Golden Master Test")    
    def test_record(self):
        for data in self.test_cases:
            name_of_first_player, name_of_second_player, score_player1, score_player2 = data
            try:
                game = TennisGame(name_of_first_player, name_of_second_player)
                result = self.check_all_scores(game, score_player1, score_player2)
            except Exception as e:
                result = type(e).__name__ + " " + str(e)

            file_name = f"{score_player1}-{score_player2}-{name_of_first_player}-{name_of_second_player}.txt"
            with open(os.path.join(self.Dir, file_name), "w") as f:
                f.write(result)
   
    def test_replay(self):
        for data in self.test_cases:
            name_of_first_player, name_of_second_player, score_player1, score_player2 = data
            try:
                game = TennisGame(name_of_first_player, name_of_second_player)
                result = self.check_all_scores(game, score_player1, score_player2)
            except Exception as e:
                result = type(e).__name__ + " " + str(e)
    
            file_name = f"{score_player1}-{score_player2}-{name_of_first_player}-{name_of_second_player}.txt"
            with open(os.path.join(self.Dir, file_name), "r") as f:
                expected = f.read()
    
            self.assertMultiLineEqual(expected, result)

    def check_all_scores(self, game, player1_score, player2_score):
        highest_score = max(player1_score, player2_score)
        for i in range(highest_score):
            if i < player1_score:
                game.won_point("player1")
            if i < player2_score:
                game.won_point("player2")

        return game.score()