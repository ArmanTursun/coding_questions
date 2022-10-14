# Easy

# Write a function that takes in a "special" array and returns its product sum.

# "Special" array is a non-empty array that contains either integers or other "special" arrays.
# The depth of a 'special' array is how far nested it is. For instance, the depth of [] is 1;
# the depth of the inner array in [[]] is 2; the depth of the innermost array in [[[]]] is 3.

# Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z);
# the product sum of [x, [y, [z]]] is x + 2 * (y + 3z).

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    return helper (array, 0, 1)

def helper(array, idx, depth):
    if idx == len(array):
        return 0

    if type(array[idx]) == int:
        return depth * array[idx] + helper(array, idx + 1, depth)
    else:
        return depth * helper(array[idx], 0, depth + 1) + helper(array, idx + 1, depth)


def productSum(array, depth = 1):
    # Write your code here.
    sum = 0
    for item in array:
        if type(item) == list:
            sum += productSum(item, depth + 1)
        else:
            sum += item
    return sum * depth

## T = O(n); S = O(d) where d is the depth