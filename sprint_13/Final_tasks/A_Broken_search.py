"""
Alla made a mistake when copying from one data structure to another. 
She stored an array of numbers in a circular buffer. The array was sorted in ascending order, 
and it was possible to find an element in logarithmic time. Alla copied the data from the ring buffer 
into a regular array, but shifted the data of the original sorted sequence. Now the array is not sorted. 
Nevertheless, we need to make sure that we can find an element in it for O(logn).

We can assume that the array contains only unique elements.

The problem should be handed in with Make compiler, it is selected by default, 
there are no other compilers in the problem. The solution is sent in a file. 
The required function signatures are in the code blanks on the disk.

You are required to implement a function which searches through a broken array. 
You can find the files with the blanks containing the function signatures and the basic test 
for the supported languages on Yandex.Disk, by following the link. 
Please note that it is not necessary to read the data and print the answer.

Search an element in sorted and rotated array using
single pass of Binary Search.
Returns index of elem in array[low..high] if elem is present,
otherwise returns -1.

Solution executes broken_search method with two input parameters:
- array to search for the element
- the element to search for
This method is slightly modified binary search,
which is suitable for searching an element in sorted rotated array. 

The logic executed inside broken_search() is following:
- while loop until left index (low) less or equal right index (high)
    - define middle element, compare with the searching one
      - if true, return middle
      else:
        - check if array[low..mid] is sorted than
          - check if elem lies in half [low..mid] or half [mid+1, high]
            - if yes: high = mid - 1
            - if no:  low = mid + 1
        - otherwise array[mid..high] must be sorted
          - check if elem lies in half [mid+1, high] or half [low..mid] 
            - if yes: low = mid + 1
            - if no:  high = mid - 1
"""


def broken_search(array: list, elem: int) -> int:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == elem:
            return mid

        # if array[low..mid] is sorted
        if array[low] <= array[mid]:
            # as this subarray is sorted, we can quickly
            # check if elem lies in that half or other half
            if elem >= array[low] and elem < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # if array[low..mid] is not sorted, then array[mid..high]
            # must be sorted
            if elem > array[mid] and elem <= array[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

