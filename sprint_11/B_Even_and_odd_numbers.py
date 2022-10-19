"""
Imagine an online subway game: the player presses a button and three random numbers appear on the screen.
If all three numbers are of the same parity, the player wins.
Write a program that determines from the three numbers whether the player has won or not.

"""

def check_parity(a: int, b: int, c: int) -> bool:
	primes = []
	if a % 2 != 0:
		primes.append(a)
	if b % 2 != 0:
		primes.append(b)
	if c % 2 != 0:
		primes.append(c)

	if len(primes) == 0 or len(primes) == 3:
		return True
	else:
		return False

def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))

