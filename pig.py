import random

random.seed(0)

def roll_die():
    return random.randint(1, 6)

def take_turn(player):
    print(f"\nPlayer {player + 1}'s turn:")
    turn_score = 0
    while True:
        roll = roll_die()
        if roll == 1:
            print("You rolled a 1. Turn over.")
            return 0
        print(f"You rolled a {roll}.")
        turn_score += roll
        print(f"Your current score for this turn is {turn_score}.")
        decision = input(f"Your total score is {players[player]}. Press (r) to roll or (h) to hold ")
        while decision not in ['r', 'h']:
            print("Invalid input. Please enter (r) to roll or (h) to hold.")
            decision = input(f"Your total score is {players[player]}. Press (r) to roll or (h) to hold ")
        if decision == "h":
            players[player] += turn_score
            return turn_score

def play_game(num_players):
    scores = [0] * num_players
    player = 0
    while max(scores) < 100:
        print(f"\nCurrent scores: {scores}")
        turn_score = take_turn(player)
        scores[player] += turn_score
        print(f"Player {player + 1}'s score is now {scores[player]}")
        if scores[player] >= 100:
            print(f"Player {player + 1} wins!")
            return
        player = (player + 1) % num_players

if __name__ == "__main__":
    num_players = int(input("How many players? "))
    players = [0] * num_players

    play_game(num_players)
