from app.modules.player import Player

def play_game(player_1, player_2):
    if player_1.choice == player_2.choice:
        return "Draw"
    elif player_1.choice == "Rock" and player_2.choice == "Paper":
            return player_2
    elif player_1.choice == "Paper" and player_2.choice == "Scissors":
            return player_2
    elif player_1.choice == "Scissors" and player_2.choice == "Rock":
            return player_2
    else:
        return player_1