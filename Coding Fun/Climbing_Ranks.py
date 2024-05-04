import pandas as pd


# Function which does a Dense Ranking on a given array.
def climb_ranks(arr1, arr2):
    """
    Takes an array of scores for given number of players and alice scores for given number of games as input and
    output our rank on each game based on the score following Dense Ranking method.
    :param arr1: Scores of 'n' number of players
    :param arr2: Scores of alice for 'm' number of games
    :return: 'm' integers where each integer indicates alice rank for the game
    """
    # List to contain and return Alice's ranks.
    results = []

    # Unique values from scores, since duplicate scores will have same rank (their index value).
    leaderboard = sorted(set(arr1), reverse=True)

    # Use this var to track index within leaderboard later.
    l = len(leaderboard)

    # Loop through each of Alice's scores
    for a in arr2:

        # If Alice's score is >= the score at the index of the end of leaderboard...
        # Subtract 1 from that index value (which is also the rank) to check the next score up.
        # If the score is less than the next score up, the index (rank) will be added to results.
        while (l > 0) and (a >= leaderboard[l - 1]):
            l -= 1

        # We add 1 to the appended value to account for 0-indexing.
        results.append(l + 1)

    return results


if __name__ == '__main__':
    n = int(input('Enter the number of players: '))
    scores = list(map(int, input().rstrip().split()))
    m = int(input('Enter the number of games alice is going to play: '))
    scores_alice = list(map(int, input().rstrip().split()))
    print(climb_ranks(scores, scores_alice))
