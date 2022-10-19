"""
Timofey wrote down two numbers in binary notation and asked Gosha to print their sum, also in binary notation. 
The built-in binary addition feature of the programming language cannot be used. Help Gosha solve the problem.
The solution must work for O(N), where N is the number of digits of the maximum number in the input.
"""

from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
	diff = len(first_number) - len(second_number)
	if diff < 0:
		first_number = first_number.rjust(len(first_number)+abs(diff),'0')
	elif diff > 0:
		second_number = second_number.rjust(len(second_number)+abs(diff),'0')
	sum_str = ''
	star = False
	for i in range(len(first_number)-1, 0-1, -1):
		if first_number[i] == '0' and second_number[i] == '0':
			if star == False:
				sum_str = sum_str + '0'
			if star == True:
				sum_str = sum_str + '1'
				star = False
		if first_number[i] != second_number[i]:
			if star == False:
				sum_str = sum_str + '1'
			if star == True:
				sum_str = sum_str + '0' 
		if first_number[i] == '1' and second_number[i] == '1':
			if star == False:
				sum_str = sum_str + '0'
			if star == True:
				sum_str = sum_str + '1'
			star = True
	if star == True:
		sum_str = sum_str + '1'
	sum_str = sum_str[::-1]
	return sum_str   
    

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
