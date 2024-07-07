# -*- coding: utf-8 -*-

import pytest
from main.tennis_game import TennisGame1

from tennis_unittest import test_cases, play_game

def writetofile(filename, score):
    with open(filename, 'w') as file:
        file.write(score)
def getFileName(score, p1Name, p2Name):
    return f"test_get_score_game1_{score}_{p1Name}_{p2Name}.txt"
    
@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game1(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
    writetofile(getFileName(score, p1Name, p2Name), game.score())
    assert score == game.score()

