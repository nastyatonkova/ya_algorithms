"""
Each island in the Algosa archipelago has some number of people living on it, or the island is uninhabited 
(then there are 0 people living on the island). Let the i-th island have ai population. 
Timothy wanted to find the median among all values of the population.

Definition: The median (https://ru.wikipedia.org/wiki/Медиана_(statistic)) of an array of numbers a_i 
is such a number that half of the numbers in the array are not larger than it, and the other half are not smaller. 
In general, the median of an array can be found by sorting the numbers and taking the average of them. If the number of numbers is even, 
take as the median the half-sum of the neighboring average numbers, (a[n/2] + a[n/2 + 1])/2.

Timothy already has separate data for the northern part of the archipelago and for the southern part, 
and the population values in each group are sorted in descending order.

Determine the median population for all the islands of Algos.

Hint: If n is the number of islands in the northern part of the archipelago and m islands 
in the southern part, your solution should work for O(log(n+m)).   
"""


import sys
def merge_iter(arr1, arr2):
    l = 0
    r = 0

    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            yield arr1[l]
            l += 1
        else:
            yield arr2[r]
            r += 1

    for i in range(l, len(arr1)):
        yield arr1[i]

    for i in range(r, len(arr2)):
        yield arr2[i]
def median(arr1, arr2):
    if (len(arr1) + len(arr2)) % 2 == 0:
        target_1_idx = (len(arr1) + len(arr2)) // 2
        target_2_idx = target_1_idx - 1
        target_1 = None
        target_2 = None
        for n, val in enumerate(merge_iter(arr1, arr2)):
            if n == target_1_idx:
                target_1 = val
            if n == target_2_idx:
                target_2 = val

            if target_1 is not None and target_2 is not None:
                return (target_1 + target_2) / 2
    else:
        target_idx = (len(arr1) + len(arr2)) // 2

        for n, val in enumerate(merge_iter(arr1, arr2)):
            if n == target_idx:
                return val
def main():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())

    north = list(map(int, sys.stdin.readline().rstrip().split()))
    south = list(map(int, sys.stdin.readline().rstrip().split()))

    print('{0:g}'.format(median(north, south)))

if __name__ == '__main__':
    main()
