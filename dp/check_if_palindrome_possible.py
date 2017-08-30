"""
There should be atmost one characters that occurs odd number of times.
All the other characters should occur even number of times.
"""

from collections import Counter 
def can_for_palindrome(string):
    count = Counter(string)
    odds = 0
    for key, value in count:
        if value%2:
            odd += 1
    return odd <= 1
