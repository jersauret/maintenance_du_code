#CONSTANTS
def get_score_language(key, language):
    translations = {
    "win_player1": {"en":WIN_FOR_PLAYER1,"fr": WIN_FOR_PLAYER1_FR},
    "win_player2": {"en":WIN_FOR_PLAYER2,"fr": WIN_FOR_PLAYER2_FR},
    "equality15": {"en":LOVE_ALL,"fr": LOVE_ALL_FR},
    "equality30": {"en":FIFTEEN_ALL,"fr": FIFTEEN_ALL_FR},
    "equality40": {"en":THIRTY_ALL,"fr": FIFTEEN_ALL_FR},
    "deuce": {"en":DEUCE,"fr": DEUCE_FR},
    "0": {"en":LOVE,"fr": LOVE_FR},
    "1": {"en":FIFTEEN,"fr": FIFTEEN_FR},
    "2": {"en":THIRTY,"fr": THIRTY_FR},
    "3": {"en":FORTY,"fr": FORTY_FR},
    "advantage_player1": {"en":ADVANTAGE_PLAYER1,"fr": ADVANTAGE_PLAYER1_FR},
    "advantage_player2": {"en":ADVANTAGE_PLAYER2,"fr": ADVANTAGE_PLAYER2_FR},
}

    
    if key in translations:
        if language in translations[key]:
            return translations[key][language]
        else:
            return "Language not found"
    else:
        return "Translation not found"

LOVE = "Love"
FIFTEEN = "Fifteen"
THIRTY = "Thirty"
FORTY = "Forty"
ADVANTAGE_PLAYER1 = "Advantage player1"
ADVANTAGE_PLAYER2 = "Advantage player2"
LOVE_ALL = "Love-All"
FIFTEEN_ALL = "Fifteen-All"
THIRTY_ALL = "Thirty-All"
DEUCE = "Deuce"
WIN_FOR_PLAYER1 = "Win for player1"
WIN_FOR_PLAYER2 = "Win for player2"
#END OF CONSTANTS

#CONSTANTS FR
LOVE_FR = "Zero"
FIFTEEN_FR = "Quinze"
THIRTY_FR = "Trente"
FORTY_FR = "Quarante"
ADVANTAGE_PLAYER1_FR = "Avantage joueur1"
ADVANTAGE_PLAYER2_FR = "Avantage joueur2"
LOVE_ALL_FR = "Zero-Partout"
FIFTEEN_ALL_FR = "Quinze-Partout"
THIRTY_ALL_FR = "Trente-Partout"
DEUCE_FR = "Egalite"
WIN_FOR_PLAYER1_FR = "Victoire joueur1"
WIN_FOR_PLAYER2_FR = "Victoire joueur2"
#END OF CONSTANTS FR
winners = {
    "player1": WIN_FOR_PLAYER1,
    "player2": WIN_FOR_PLAYER2

}
equality_table = {
    0: LOVE_ALL,
    1: FIFTEEN_ALL,
    2: THIRTY_ALL,
    3: DEUCE,
}

scores_text = {
    0: LOVE,
    1: FIFTEEN,
    2: THIRTY,
    3: FORTY
}




