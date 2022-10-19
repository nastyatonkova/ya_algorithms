"""
Vasya is doing a math test: he calculates the value of functions at different points. 
The weather is fine, and his friends call him for a walk. But the boy decided to finish the test first and only then go to his friends. 
Unfortunately, Vasya can not yet know how to program. But you can. Help Vasya to write the code of a function that calculates y = ax2 + bx + c. 
Write a program that will, by the coefficients a, b, c and the number x, print the value of the function at the point x. 

"""

def evaluate_function(a: int, b: int, c: int, x: int) -> int:
	return a * x ** 2 + b * x + c

a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, b, c, x))
