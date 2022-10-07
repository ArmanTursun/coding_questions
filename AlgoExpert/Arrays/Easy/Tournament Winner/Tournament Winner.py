# There's an algotithms tournament taking place in which teams of programmers compete aggains each other to solve algorithmic
# problems as fast as possible. Teams compete in a round robin, where each team faces off against all other teams.
# Only two reams compete aginst each other at a time, and for each competetion, one team is designated the home team, while
# the other team is the away team. In each ompetition, there's always one winner and one loser; there are no ties. A team
# receives 3 points if it wins and 0 point if lt loses. The winner of the tournament is the team that receives the most points.

# Given an array of pairs representing the teams that have competed against each other and an array containing the results of
# each competition, write a function that returns the winner of the tournment. The input arrays of wach competition, write a
# function that returns the winner of the tournment. The input arrays are named 'competitions' and 'results'. respectively.
# The 'competitions' array has elements in the form of [homeTeam, awayTeam], where each team is a string of at most 30 characters
# representing the name of the team. The results array contains information about the winner of each corresponding competition
# in the 'competitions[i]', where a 1 in the results array means that the home team in the corresponding copetition won and a 0
# means that the away team won.

# It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once.
# It's also guaranteed that the tournament will always have at least two teams.

# Sample Input
#   competitions = [
#     ["HTML", "C#"],
#     ["C#", "Python"],
#     ["Python", "HTML"]
#   ]
#   results = [0, 0, 1]

# Sample Output
# 'Python'

def tournamentWinner(competitions, results):
    # Write your code here.
    final_winner = ['', 0]
    points = {}
    for compet, result in zip(competitions, results):
        winner = compet[not result]
        if winner not in points:
            points[winner] = 0
        points[winner] += 3

        if points[winner] > final_winner[1]:
            final_winner = [winner, points[winner]]

    return final_winner[0]

## T = O(n); S = O(k)
## where n is the number of competitions
## k is the number of teams

