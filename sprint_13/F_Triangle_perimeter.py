"""
Before going to bed, Rita decided to play a game on her phone. 
There is an array of integers in which each element denotes the length of a side of a triangle. 
Find the maximum possible perimeter of a triangle made up of sides with lengths from the given array. 
Help Rita finish the game quickly and go to bed.

Recall that three segments with lengths a ≤ b ≤ c can be made into a triangle if the triangle inequality is satisfied: c < a + b

Consider this example:
We are given the lengths of the sides 6, 3, 3, 2. Let us try to choose 6 as the longest side. 
The triangle inequality cannot hold because there remain 3, 3, 2 -- the maximal sum of them is 6.

Without the 6, the remaining three segments already form a triangle with sides 3, 3, 2. 
The inequality holds: 3 < 3 + 2. The perimeter is 3 + 3 + 2 = 8.  
"""


with open("input.txt") as f:
    len_arr = int(f.readline())
    arr = sorted([int(elem) for elem in f.readline().split()], reverse=True)

max_p = 0
for i in range(len_arr-2):
    if arr[i] < arr[i+1] + arr[i+2]:
        max_p = arr[i] + arr[i+1] + arr[i+2]
        break

print(max_p)
