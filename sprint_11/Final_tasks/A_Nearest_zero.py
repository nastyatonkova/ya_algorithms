"""
Timothy is looking for a place to build himself a house. 
The street he wants to live on has length n, that is, it consists of n identical consecutive plots. 
Each plot is either empty, or a house has already been built on it.
Social Timothy doesn't want to live far away from other people on that street. 
That's why for each lot he needs to know the distance to the nearest empty lot. 
If the plot is empty, this value will be zero - the distance to himself.
Help Timothy calculate the distances he is looking for. 
You have a street map for this purpose. The houses in Timothy's city were numbered in the order 
in which they were built, so their numbers on the map are not ordered in any way. 
Blank areas are marked with zeros.

The following algorithm is used:

iterate through the sequence of houses from left to right;
for sequence[i] != 0 fill result distance with increasing sequence (1,2,..),
refresh it (start from 1) when 0 occures in sequence;
for sequence[i] = 0 define system state {no zeroes, one zero, multiple zeroes}
and update result distance values in the following way:
no zeroes - no update,
one zero - reverse values before 0 occures,
multiple zeroes - update the second half of distancies between 2 zeroes
with reversed values of the first half.

"""


from typing import List, Tuple, NoReturn


def nearest_null(n: int, sequence: List[int]) -> List[int]:

    result_dist = [0] * n
    pos_zero = -1 # not defined
    system_state = 0 # no zeroes

    for i in range(n):
    
        if sequence[i] != 0:
            if pos_zero >= 0:
                # do for state=..0hh
                result_dist[i] = i+1 - pos_zero
            else:
                # do for state=0hh
                result_dist[i] = i+1
    
        if sequence[i] == 0:
            # define system state {no zeroes, one zero, multiple zeroes}
            if system_state == 0:
                system_state = 1
            elif system_state == 1:
                system_state = 2
        
            result_dist[i] = 0

            # do for state=0hh0
            if system_state == 2:
                half_dist = (i - pos_zero) // 2
                # reversed second half of sequence between zeroes equal to first half
                result_dist[i-1:i-1-half_dist:-1] = result_dist[pos_zero:pos_zero+half_dist]
            
            pos_zero = i+1
        
            # next iteration if sequence(i=0)==0
            if i == 0:
                continue;
        
            # do for state=hh0
            if system_state == 1:
                result_dist[:i] = result_dist[i-1::-1]
	
    return result_dist


def read_input() -> Tuple[int, List[int]]:
    with open('input.txt') as input_file:
        n = int(input_file.readline().strip())
        sequence = list(map(int, input_file.readline().strip().split()))
    return n, sequence

def write_result(result: List[int]) -> NoReturn:
    with open('output.txt', 'w') as out_file:
        out_file.write(" ".join(map(str, result)))

if __name__ == '__main__':
    result = nearest_null(*read_input())
    write_result(result)
