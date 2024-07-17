import os
import unittest

from tennis_game_multi import TennisGameMulti as TennisGame


class GoldenMasterTest(unittest.TestCase):
    Dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "expectedresults_fr")
    print(Dir)

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def setUp(self):
        self.test_cases = self.generate_test_cases()
        self.test_cases_fr = self.generate_test_cases_fr()

    def tearDown(self):
        self.test_cases = None
        self.test_cases_fr = None

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

    @staticmethod
    def generate_test_cases_fr():
        test_cases_fr = []
        for player1_score in range(21):
            for player2_score in range(21):
                test_cases_fr.append(("player1", "player2", player1_score, player2_score))
                test_cases_fr.append(("player2", "player1", player1_score, player2_score))
                test_cases_fr.append(("", "player1", player1_score, player2_score))
                test_cases_fr.append(("player1", "", player1_score, player2_score))
        return test_cases_fr

    @unittest.skip("Skipping test_record")
    def test_record(self):
        for data in self.test_cases:
            player1_name, player2_name, player1_score, player2_score = data
            try:
                game = TennisGame(player1_score, player2_score, player1_name, player2_name)
                result = game.get_current_score_display()
            except Exception as e:
                result = type(e).__name__ + " " + str(e)

            file_name = f"{player1_score}-{player2_score}-{player1_name}-{player2_name}.txt"
            with open(os.path.join(self.Dir, file_name), "w") as f:
                f.write(result)
    @unittest.skip("Skipping test_record")
    def test_record_fr(self):
        for data in self.test_cases_fr:
            player1_name, player2_name, player1_score, player2_score = data
            try:
                game = TennisGame(player1_score, player2_score, player1_name, player2_name)
                result = game.get_current_score_display()
            except Exception as e:
                result = type(e).__name__ + " " + str(e)

            file_name = f"{player1_score}-{player2_score}-{player1_name}-{player2_name}.txt"
            with open(os.path.join(self.Dir, file_name), "w") as f:
                f.write(result)

    def test_replay(self):
        self.setUp()
        for data in self.test_cases:
            player1_name, player2_name, player1_score, player2_score = data
            try:
                game = TennisGame(player1_score, player2_score, player1_name, player2_name)
                result = game.get_current_score_display()
                print(data)
            except Exception as e:
                result = type(e).__name__ + " " + str(e)

            file_name = f"{player1_score}-{player2_score}-{player1_name}-{player2_name}.txt"
            with open(os.path.join(self.Dir, file_name), "r") as f:
                expected = f.read()
            print(self.assertMultiLineEqual(expected, result))
