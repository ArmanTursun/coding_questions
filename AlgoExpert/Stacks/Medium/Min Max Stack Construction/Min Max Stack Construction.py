# Medium

# Write a MinMaxStack class for a Min Max Stack. The class should support:
#   - Pushing and popping values on and off the stack.
#   - Peeking at the value at the top of the stack.
#   - Getting both the minimum and the maximum values in the stack at any given point in time.

# All class methods, when considered independently, should run in constant time and with constant space.

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.max = []
        self.min = []

    def peek(self):
        # Write your code here.
        if not self.stack:
            return None
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        if not self.stack:
            return None
        self.min.pop()
        self.max.pop()
        return self.stack.pop()

    def push(self, number):
        # Write your code here.
        self.stack.append(number)
        cur_max = cur_min = number
        if self.max and self.min:
            cur_max = max(self.max[-1], number)
            cur_min = min(self.min[-1], number)
        self.max.append(cur_max)
        self.min.append(cur_min)

    def getMin(self):
        # Write your code here.
        return self.min[-1]

    def getMax(self):
        # Write your code here.
        return self.max[-1]
