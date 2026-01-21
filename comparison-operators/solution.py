"""
Problem: Comparison Operators
URL: https://neetcode.io/problems/python-comparison-operators/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def check_greater_than_or_equal(x, y) -> bool:
    return(x>=y)


# Don't change below this line
print("2 is equal to 2:", check_equal(2, 2))
print("-2 is equal to 2:", check_equal(-2, 2))

print("-2 is not equal to 2:", check_not_equal(-2, 2))
print("2 is not equal to 2:", check_not_equal(2, 2))
