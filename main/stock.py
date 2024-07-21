import pytest

from main.tennis_game import TennisGame
from main.tennis_game_multi import TennisGameMulti
from test_tennis import test_cases


def writetofile(file_name, score):
    with open(file_name, 'w') as file:
        file.write(score)


def getFileName(score, p1_name, p2_name):
    return f"test_get_score_game1_{score}_{p1_name}_{p2_name}.txt"


@pytest.mark.parametrize('p1_points p2_points score p1_name p2_name'.split(), test_cases)
def test_get_score_game(p1_points, p2_points, score, p1_name, p2_name):
    game = TennisGameMulti(p1_points, p2_points, p1_name, p2_name)
    writetofile(getFileName(score, p1_name, p2_name), game.get_current_score_display())
    assert score == game.get_current_score_display()
