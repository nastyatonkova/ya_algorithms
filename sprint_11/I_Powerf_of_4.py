"""
Write a program that determines whether a positive integer is a power of four.
Hint: The degree of a four is all numbers of the form 4^n, where n is a non-negative integer.
"""

def is_power_of_four(number: int) -> bool:
	while number > 3:
		number = number / 4
	if number == 1:
		return True
	return False

print(is_power_of_four(int(input())))
