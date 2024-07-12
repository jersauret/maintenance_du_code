# -*- coding: utf-8 -*-

import pytest

from main.tennis_game import TennisGame
from tennis_unittest import test_cases, play_game


@pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
def test_get_score_game1(p1Points, p2Points, score, p1Name, p2Name):
    game = play_game(TennisGame, p1Points, p2Points, p1Name, p2Name)
    assert score == game.score()