# Easy

# You're given a string of available characters and a string representing a document that you
# need to generate. Write a function that determines if you can generate the document using
# available characters. If you can generate the document, your function should return True;
# otherwise, it should return False.

# You're only able to generate the document if the frequency of unique characters in the
# characters string is greater than or euqal to the frequency of unique characters in the
# document string.

# Note that you can always generate the empty string ("").

def generateDocument(characters, document):
    # Write your code here.
    map = {}
    for ch in characters:
        if ch not in map:
            map[ch] = 1
        else:
            map[ch] += 1

    map_doc = {}
    for ch in document:
        if ch not in map or not map[ch]:
            return False
        map[ch] -= 1

    return True

# T = O(n + m); S = O(c) where n is the length of characters
# m is the length of document
# c is the number of unique characters in characters
