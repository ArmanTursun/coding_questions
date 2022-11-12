# Hard

# Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student
# scores on the final exam in a particular order (not necessarily sorted), and you want to reward your
# students. You decide to do so fairly by giving them arbitrary rewards following two rules:
#   - All students must receive at least one reward.
#   - Any given student must receive strictly more rewards than an adjacent student with a lower score
#       and must receive strictly fewer rewards than an adjacent student with a higher score.

# Write a function that takes in a list of scores and returns the minimum number of rewards that you
# must give out to students to satisfy the two rules.
# You can assume that all students have different scores; in other words, the scores are all unique.

# Sample Input
# scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]

# Samole Input
# 25 // rewards = [4, 3, 2, 1, 2, 3, 4, 5, 1]

def minRewards(scores):
    # Write your code here.
    if len(scores) == 1:
        return 1
    rewards = [0 for score in scores]

    for i in range(len(scores)):
        if i == 0 and scores[i] < scores[i + 1]:
            rewards[i] = 1
        elif i == len(scores) - 1 and scores[i] < scores[i - 1]:
            rewards[i] = 1
        elif scores[i] < scores[i - 1] and scores[i] < scores[i + 1]:
            rewards[i] = 1

    for i in range(len(rewards)):
        if rewards[i] == 1:
            addRewards(i, rewards, scores)
    return sum(rewards)

def addRewards(idx, rewards, scores):
    left = idx - 1
    right = idx + 1
    while left > -1 and scores[left] > scores[left + 1] and rewards[left] <= rewards[left + 1]:
        rewards[left] = rewards[left + 1] + 1
        left -= 1
    while right < len(rewards) and scores[right] > scores[right - 1]:
        rewards[right] = rewards[right - 1] + 1
        right += 1
## T = O(n); S = O(n)


def minRewards(scores):
    # Write your code here.
    rewards = [1 for _ in scores]

    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in range(len(scores) - 2, -1, -1):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)
## T = O(n); S = O(n)