"""

On the keypad of the old cell phones, each number corresponded 
to several letters. It goes something like this:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'.

You know the order in which the phone buttons were pressed, 
not counting the repetitions. 
Type all combinations of letters that can be typed in this sequence of keystrokes.  
"""


def letterCombinations(digits):

    letters = {'2':'abc', '3':'def','4':'ghi', 
               '5':'jkl', '6':'mno', '7':'pqrs',
               '8':'tuv', '9':'wxyz'}

    def backtrack(digits, path, res):
        if digits == '':
            res.append(path)
            return
        for letter in letters[digits[0]]:

            path += letter
            backtrack(digits[1:], path, res)
            path = path[:-1]
    res = []
    backtrack(digits, '', res)
    for x in res:
        print(x, end=' ')

input_digits = (input())
letterCombinations(input_digits) 
