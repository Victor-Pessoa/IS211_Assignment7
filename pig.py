import argparse
import random

random.seed(0)


def get_args():
    parser = argparse.ArgumentParser(description='Play a game of Pig!')
    parser.add_argument('--numPlayers', type=int, default=2, help='Number of players')
    return parser.parse_args()


def roll():
    return random.randint(1, 6)


def play(playerScores):
    currentPlayer = 0
    currentScore = 0

    while max(playerScores) < 100:
        print(f"\nPlayer {currentPlayer + 1}'s turn:")
        print(f"Current score for this turn: {currentScore}")
        print(f"Player scores: {playerScores}")

        decision = input("Enter 'r' to roll or 'h' to hold: ")
        if decision == 'r':
            rollResult = roll()
            print(f"Player {currentPlayer + 1} rolled a {rollResult}")

            if rollResult == 1:
                print("Rolled a 1. Turn over, no points earned.")
                currentScore = 0
                currentPlayer = (currentPlayer + 1) % numPlayers
            else:
                currentScore += rollResult

        elif decision == 'h':
            playerScores[currentPlayer] += currentScore
            print(f"Player {currentPlayer + 1} scored {currentScore} points this turn")
            currentScore = 0
            currentPlayer = (currentPlayer + 1) % numPlayers

    print(f"\nPlayer {playerScores.index(max(playerScores)) + 1} wins with {max(playerScores)} points!")


if __name__ == '__main__':
    args = get_args()
    numPlayers = args.numPlayers
    playerScores = [0] * numPlayers
    play(playerScores)
