# Easy

# It's photo day, and you're the photographer. Half of the students wearing red and the other
# half wearing blue. You're responsible for arranging the students in two rows before taking
# the photo. Each row should contain the same number of the students and should adhere to the
# following guildelines:
# 1. All students wearing red shirts or wearing blue shirts must be in the same row repectively.
# 2. Each student in the back row must be strictly taller than the student infront of them.

# You're given two input arrays: heights of red and blue.
# Write a function return whether can photo that follows the stated guildlines can be taken.

# Sample Input
# redShirtHeights = [5, 8, 1, 3, 4]
# blueShirtHeights = [6, 9, 2, 4, 5]

# Sample Output
# true

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    firstRowRed = True

    if redShirtHeights[0] > blueShirtHeights[0]:
        firstRowRed = False

    for i in range(len(redShirtHeights)):
        if firstRowRed != (redShirtHeights[i] < blueShirtHeights[i]):
            return False

    return True
