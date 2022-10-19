"""

To choose the best algorithm for the problem, Gosha continued to study different sorts. 
Next is the bubble sorting - https://ru.wikipedia.org/wiki/Сортировка_пузырьком.

Its algorithm is as follows (we sort by non-decreasing):

    At each iteration we go through the array, comparing pairs of neighboring elements one by one. 
    If the element at position i is larger than the one at position i + 1, swap them. 
    After the first iteration, the largest element will appear at the end of the array.
    We go through the array performing the above actions until the next iteration shows that exchanges 
    are no longer needed, i.e. the array is already sorted.
    After no more than n - 1 iterations the execution of the algorithm ends, 
    because at each iteration at least one element turns out to be in the correct position.


Help Gosha write the code of the algorithm.   
"""


def bubble_sort(number, source_array):
    flag = 1
    for i in range(number - 1):
        for j in range(0, number-i-1):
            if source_array[j] > source_array[j+1]:
                source_array[j], source_array[j+1] = source_array[j+1], source_array[j]
                flag = 1
        if flag == 1:
            for x in source_array:
                print(x, end=' ')
            print('')
            flag = 0


if __name__ == '__main__':
    number = int(input())
    source_array = [int(num) for num in input().split(' ')]
    bubble_sort(number, source_array)
