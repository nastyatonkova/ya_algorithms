"""

Gosha was given the task of writing a nice merge sort. 
So Gosha has to implement merge function and merge_sort function separately.

    The merge function takes two sorted arrays, merges them into one sorted array and returns it. 
    If the required signature is of the form merge(array, left, mid, right), then the first array is given by the half-interval 
    [left,mid] of the array, and the second one by the half-interval [mid,right) of the array.
    The merge_sort function accepts some subarray to be sorted. The subarray is specified by a half-interval - its beginning and end. 
    The function must sort the subarray passed to it, it returns nothing.
    The merge_sort function splits the half-interval into two halves and recursively calls sorting separately for each one. 
    The two sorted arrays are then merged into one using merge.

Note that it is the half-intervals [begin,end] that are passed to the function, i.e., 
the right end is not included. For example, if you call merge_sort(arr, 0, 4), where arr=[4,5,3,0,1,2], 
only the first four elements will be sorted, the modified array will look like arr=[0,3,4,5,1,2].

Implement these two functions.   
"""


def merge(arr, lf, mid, rg):
  result = []
  left = arr[lf:mid]
  right = arr[mid:rg]
  ileft = iright = 0
  while len(result) < len(left) + len(right):
    if left[ileft] <= right[iright]:
      result.append(left[ileft])
      ileft += 1
    else:
      result.append(right[iright])
      iright += 1
    if iright == len(right):
      result += left[ileft:]
      break
    if ileft == len(left):
      result += right[iright:]
      break
  return result


def merge_sort(arr, lf, rg):
  if rg - lf >= 2:
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    arr[lf:rg] = merge(arr, lf, mid, rg)


def test():
  a = [1, 4, 9, 2, 10, 11]
  b = merge(a, 0, 3, 6)
  expected = [1, 2, 4, 9, 10, 11]
  assert b == expected
  
  c = [1, 4, 2, 10, 1, 2]
  merge_sort(c, 0, 6)
  expected = [1, 1, 2, 2, 4, 10]
  assert c == expected


if __name__ == '__main__':
  test()
