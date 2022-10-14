# Easy

# Write a function that takes in a non-empty string and returns its run-length encoding.
# Run-length encoding is a form of lossless date compression in which runs of date are
# stored as a single data value and count, rather than as the original run. For this problem,
# a run of data is any sequence of consecutive, identical characters. So the run "AAA" would be
# run length encoded as "3A".

# To make thins more complicated, however, the input string can contain all sorts of special
# characters, including numebers. And since encoded data must be decodable, this means that
# we can't naively run-length-encode long runs. For example, the run "AAAAAAAAAAAA" (12 As),
# can't naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA"
# or "1AA". Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion;
# the aforementioned run should be encoded as "9A3A".

# Sample Input
# string = "AAAAAAAAAAAAABBCCCCDD"

# Sample Output
# "9A4A2B4C2D"

def runLengthEncoding(string):
    # Write your code here.
    cur_letter = None
    count = 0
    coded = ''

    for letter in string:
        if not cur_letter or count < 9 and cur_letter == letter:
            count += 1
            cur_letter = letter

        if count == 9:
            coded += ('9' + cur_letter)
            count = 0
            cur_letter = None
        elif cur_letter != letter:
            coded += (str(count) + cur_letter)
            cur_letter = letter
            count = 1
    coded += (str(count) + cur_letter)
    return coded

## T = O(n); S = O(n)