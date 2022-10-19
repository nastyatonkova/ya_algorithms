"""


The task is related to reverse Polish notation. It is used for parsing arithmetic expressions. 
It is also sometimes called postfix notation.

In postfix notation, the operands are in front of the operation signs.
To calculate the value of an expression written in reverse polish notation, 
the expression must be read from left to right, and the following steps must be followed:

    Handling the input character:
        If an operand is given as input, it is placed at the top of the stack.
        If an operation character is given as input, this operation is performed 
        on the required number of values taken from the stack in order of addition. 
        The result of the operation is placed on the top of the stack.

    If the input character set is not completely processed, skip to step 1.
    After complete processing of the input character set, the result of expression calculation 
    is placed at the top of the stack. If there are several numbers left in the stack, 
    only the top element must be output.


For the solution of this task standart stack class is used 
(push and pop methods). 
 
Dictionary <operators> (+,-,/,*) is defined. 
 
Input data splited by white space forms list and 
is used as an argument in method <calc>. 
 
In the method <calc> we iterate exp (expresion) through the list with input data: 
- if the exp is number, it adds to the stack 
- if the exp is operator (in the corr. dict), than  
-- get 2 last elements from the stack (pop) and do calculation with them 
-- put the result on top of the stack (push) 
That way the final result would be on top of stack. 
 
! It is assumed the correctness of input data, 
for example  
- input {1 + -} leads to an error 
- input {1 1 1 +} leads to wrond answer 
"""


import operator 
from typing import List 
 
 
class Stack: 
     
    def __init__(self): 
        self.__items = [] 
 
    def push(self, value: int): 
        self.__items.append(value) 
 
    def pop(self): 
        return self.__items.pop() 
 
 
operators = { 
        '+': operator.add, 
        '-': operator.sub, 
        '*': operator.mul, 
        '/': operator.floordiv, 
    } 
 
def calc(expression: List[str]) -> int: 
    stack = Stack() 
    for exp in expression: 
        if exp in operators: 
            operand_2 = stack.pop() 
            operand_1 = stack.pop() 
            func = operators.get(exp) 
            stack.push(func(operand_1, operand_2)) 
        else: 
            stack.push(int(exp)) 
    return stack.pop() 
 
def input_data() -> List[str]: 
    return input().rstrip().split() 
 
if __name__ == '__main__': 
    print(calc(input_data())) 
