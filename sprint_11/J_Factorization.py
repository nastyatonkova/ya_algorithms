"""
The basic theorem of arithmetic says: any number is decomposed into a product 
of prime factors in a single way, up to their permutation. For example:

    The number 8 can be represented as 2 × 2 × 2.
    The number 50 is 2 × 5 × 5 (or 5 × 5 × 2, or 5 × 2 × 5). 
    The three variants differ only in the order of the multipliers.

Decomposition of a number into prime factors is called factorization of a number.
Write a program that factorizes the number you pass in.
"""

from typing import List

def factorize(number: int) -> List[int]:
	devisors = []
	div = 2
	while number >= div * div:
		while number % div == 0:
			devisors.append(div)
			number = number//div
		div += 1
	if number > 1:
		devisors.append(number)
	return devisors

result = factorize(int(input()))
print(" ".join(map(str, result)))
