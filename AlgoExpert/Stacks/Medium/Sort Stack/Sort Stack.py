# Medium

# Write a function that takes in an array of integers representing a stack, recursively sorts the stack in place,
# and returns it. The array must be treated as a stack, with the end of the array as the top of the stack.
# Therefore, you're only allowed to
#   - Pop elements from the top of the stack by removing elements from the end of the array using the built-in
#     .pop() method in your programming language of choice.
#   - Push elements to the top of the stack by appending elements to the end of the array using the built-in
#     .append() method in your programming language of choice.
#   - Peek at the element on top of the stack by accessing the last element in the array.

# You're not allowed to perform any other operations on the input array, including accessing elements, moving
# elements, etc.. You're also not allowed to use any other data structures, and your solution must be recursive.

# Sample Input
# stack = [-5, 2, -2, 4, 3, 1]

# Sample Output
# [-5, -2, 1, 2, 3, 4]

def sortStack(stack):
    # Write your code here.
    sortHelper(stack)
    return stack

def sortHelper(stack):
    if not stack:
        return stack
    cur_top = stack.pop()
    sortStack(stack)
    insert(stack, cur_top)

def insert(stack, cur_top):
    if not stack or stack[-1] < cur_top:
        stack.append(cur_top)
    else:
        top_pop = stack.pop()
        insert(stack, cur_top)
        stack.append(top_pop)
