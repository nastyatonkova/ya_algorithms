"""
Vasya implemented a function that converts an integer from decimal to binary. 
But it does not seem to be very optimal.
Try to write a more efficient program.
Do not use the language's built-in tools to convert numbers to binary representation.
"""

def to_binary(number: int) -> str:
	b = ''
	while number > 0:
		b = str(number % 2) + b
		number = number // 2
	return b

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
