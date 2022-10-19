"""
After Gosha learned about merge sorting and quick sorting, he decided to 
invent his own sorting method that would involve splitting the data into parts.
He named his sorting Partial.
You can use this method to sort n unique numbers a1, a2, ... , an that are in the range from 0 to n - 1.
The sorting algorithm consists of three steps:

    Divide the original sequence into k blocks B1, ..., Bk. The blocks may have different sizes. 
    If block size i is si, then B1 = { a1, ..., as1 }, B2 = { as1 + 1, ... , as1 + s2 } and so on.
    Sort each of the blocks.
    Merge blocks - write the sorted block B1 first, then B2, ... , Bk

Partial sorting is better than regular sorting if we can split the sequence into a large number of blocks in the first step. 
However, not every such partitioning is suitable. Determine the maximum number of blocks 
that you can split the original sequence to make the sorting work correctly.

Consider the following example: a = [3, 2, 0, 1, 4, 6, 5].
The minimum size of the first block B1 is 4. If you take only the first two elements, 
the sorted sequence will start with two, which is incorrect. If you take the first three elements, 
the sequence will start with zero, but it will be followed by two. The first four elements already guarantee 
the correct prefix after combining the blocks. The four can be taken as an independent block of one element. 
The last two elements must be combined into a third block. Thus:

B1 = { 3, 2, 0, 1 }
B2 = { 4 }
B3 = { 6, 5 }

In this example, the answer is 3. The maximum number of blocks is three. 
"""


with open('input.txt') as f:
    n = int(f.readline())
    arr = list(map(int, (f.readline().split())))


def maxChunksToSorted(arr):
    ans = ma = 0
    for i, x in enumerate(arr):
        ma = max(ma, x)
        if ma == i: ans += 1
    return ans

print(maxChunksToSorted(arr))
