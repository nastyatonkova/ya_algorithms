"""
Alla wanted narrow tulip beds under her window. On the plot plan, 
the flowerbeds are simply indicated by horizontal segments lying in a straight line. 
N gardeners were hired to do the landscaping. Each of them handled some segment on the scheme. 
The process was not very well organized, sometimes the same segment or part of it could be worked by several gardeners at once. 
Thus, segments processed by two different gardeners merged into one. The continuous treated section will then become a flowerbed. 
You need to define the boundaries of future beds.

Let's look at some examples.

Example 1:
Two identical segments [7,8] and [7,8] merge into one, but then they are overlapped by the segment [6,10]. 
Thus we have two flowerbeds with coordinates [2,3] and [6,10].

Example 2
The segments [2,3], [3,4] and [3,4] merge into one segment [2,4]. 
The segment [5,6] is not joined with anyone, add it to the answer.   
"""


def segmentsUnion(data):
    data.sort()

    newData = []
    start = data[0][0]
    end = data[0][1]
    for i in range(n-1):
        if end < data[i+1][0]:
            newData.append('{} {}'.format(start,end))
            start = data[i+1][0]
            end = data[i+1][1]
        elif data[i+1][1]>end:
            end = data[i+1][1]
    newData.append('{} {}'.format(start,end))
    
    return newData

n = int(input())
if n >= 1:
    data = []

    for i in range(n):
        data.append(tuple([int(x) for x in input().split(' ')]))
        
    print('\n'.join(segmentsUnion(data)), end='')
