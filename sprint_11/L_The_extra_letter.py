"""
Vasya really likes string problems, so he made up his own. 
There are two strings s and t, consisting only of lowercase letters. 
The string t is obtained by mixing letters of the string s and adding 1 letter to a random position. 
We need to find the added letter. 
"""

from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
	for letter in longer:
		if letter in shorter:
			shorter = shorter.replace(letter, '', 1)
		else:
			return letter
	return -1

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
