"""
This is the task Timofey offered at an interview to one of the candidates. 
If you haven't encountered it yet, you probably will - it's quite popular.

A bracket sequence is given. You need to determine if it is correct.

We'll stick to this definition:

    An empty string is a valid bracket sequence;
    a regular parenthesized bracket sequence of the same type is a regular bracket sequence;
    A right bracket sequence with a right bracket sequence assigned to the left or right is also a right bracket sequence.

The input is a sequence of three kinds of brackets: [], (), {}.

Write a function is_correct_bracket_seq that takes a bracket sequence as input and returns True 
if the sequence is correct and False otherwise.

"""


class BracketStack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def is_correct_bracket_seq(sequence: str) -> bool:
    if len(sequence) == 0:
        return True

    bracket_stack = BracketStack()
    brackets = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    for s in sequence:
        if s in brackets.keys():
            bracket_stack.push(s)
        else:  # Если закрывающиеся
            if bracket_stack.size() == 0:
                return False
            top_item = bracket_stack.peek()
            if brackets.get(top_item) == s:
                bracket_stack.pop()
            else:
                return False
    if bracket_stack.size() == 0:
        return True
    else:
        return False


def input_data() -> str:
    return input().rstrip()


if __name__ == '__main__':
    print(is_correct_bracket_seq(input_data()))
