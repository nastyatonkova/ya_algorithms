"""
Vasya asked Alla to help him solve a problem. This time in computer science.
For a non-negative integer X, the list form is an array of its digits from left to right. 
For example, for 1231 the list form is [1,2,3,1]. 
The input is the number of digits of number X, 
the list form of non-negative number X, and non-negative number K. The numbers K and X do not exceed 10000.

You need to return the list form of number X + K.
"""

from typing import List, Tuple

def get_sum(number_list: List[int], k: int) -> List[int]:
	number = int(''.join(map(str, number_list)))
	summa = number + k
	x = [int(a) for a in str(summa)]
	return x


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
