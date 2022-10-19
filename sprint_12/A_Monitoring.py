"""
Alla received an assignment related to monitoring the work of various servers. 
You need to understand how long it takes for certain requests to be processed on certain servers. 
This information must be stored in a matrix, where the column number corresponds to the request ID, 
and the row number corresponds to the server ID. Alla mixed up the rows and columns. It happens to everyone. Help her fix the bug.

There is a matrix of size m × n. You need to write a function that transposes it.

The transposed matrix is obtained from the original matrix by replacing the rows by the columns.

"""


def data_input():
    n = int(input())
    m = int(input())
    matrix = ''
    matrix = [input().split(' ') for j in range(n)]
    return n, m, matrix

def calculations():
    n, m, matrix = data_input()
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print('')
if __name__ == '__main__':
    calculations()
    