"""
To prepare for the seminar, Gosha needs to read an article on effective management. 
Since Gosha wants to plan the day in advance, he needs to estimate the difficulty of the article.

He came up with this method of evaluation: he takes a random sentence from the text 
and looks for the longest word in it. Its length will be the conditional complexity of the article.

Help Gosha cope with this task.

"""

def get_longest_word(line: str) -> str:
	list_of_words = line.lstrip().rstrip().split(' ') 
	#print(list_of_words)
	max_len_word = 0
	len_word = ""
	for word in list_of_words:
		if len(word) > max_len_word:
			max_len_word = len(word)
			len_word = word
	return len_word

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
	print(result)
	print(len(result))
	

print_result(get_longest_word(read_input()))
