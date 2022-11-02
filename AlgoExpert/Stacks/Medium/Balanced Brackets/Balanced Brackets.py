# Medium

# Write a function that takes in a string made up of brackets( (, [, {, ), ]. } ), and other optional characters.
# The function should return a boolean representing whether the string is balanced with regards to brackets.
# A string is said to be balanced if it has as many oprning brackets of a certain type as it has closing brackets
# of that type and if no bracket is unmatched. Note that an opening bracket can't match a corresponding closing
# bracket that comes before can't match a corresponding opening bracket that comes after it. Also, brackets can't
# overlap each other as in [(]).

# Sample Input
# string = "([])(){}(())()()"

# Sample Output
# True

def balancedBrackets(string):
    # Write your code here.
    stack = []
    for ch in string:
        if not isBracket(ch):
            continue
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
        elif ch == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif ch == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif ch == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False

    return True if not stack else False


def isBracket(character):
    if character == "(" or "[" or "{" or ")" or "]" or "}":
        return True
    else:
        return False

## T = O(n); S = O(n)