"""
Help Vasya figure out if the phrase is a palindrome. 
Only letters and numbers are taken into account, capital and lowercase letters are considered the same.
The solution must work for O(N), where N is the input string length.
"""

def is_palindrome(line: str) -> bool:
	updated_line = line.lower()
	updated_line = "".join(c for c in updated_line if c.isalnum())
	n = len(updated_line)
	for i in range(len(updated_line)//2):
		if updated_line[i] != updated_line[n-1-i]:
			return False
	return True


print(is_palindrome(input().strip()))
