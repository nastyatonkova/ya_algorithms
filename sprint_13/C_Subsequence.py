"""

Gosha likes to play the game "Sub-sequence": two lines are given, and you have to understand 
whether the first of them is a subsequence of the second one. 
When the strings are long enough, it is very difficult to get the answer to this question 
just by looking at them. Help Gosha write a function that solves this problem.   
"""


def subsequence(substring, whole_line):
    position = -1
    for i in substring:
        position = whole_line.find(i, position + 1)
        if position == -1:
            return False
    return True

substring = input()
whole_line = input()

print(subsequence(substring, whole_line)) 
