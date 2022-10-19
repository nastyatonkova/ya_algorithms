"""
A matrix is given. You need to write a function that returns all its neighbors for an element. 
An element that is one cell to the left, right, up or down from the current one is considered a neighbor. Diagonal elements are not considered neighbors.
For example, in matrix A, the neighboring elements for (0, 0) are 2 and 0, and for (2, 1) are 1, 2, 7, 7. 
"""

from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
	list_neighbours = []
	n = len(matrix)-1
	m = len(matrix[0])-1
    # get left neighbour
	if col > 0:
		list_neighbours.append(matrix[row][col-1])
	# get right neighbour
	if col < m:
		list_neighbours.append(matrix[row][col+1])
	# get bottom neighbour
	if row < n:
		list_neighbours.append(matrix[row+1][col])
	# get upper neighbour
	if row > 0:
		list_neighbours.append(matrix[row-1][col])
	return sorted(list_neighbours)



def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col

matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))

