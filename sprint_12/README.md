# **Yandex.Practicum. Sprint 12**

# Basic data structures
https://contest.yandex.ru/contest/23389/problems/

## A. Monitoring:
There is a matrix of size m × n. You need to write a function that transposes it.

The first line contains n - the number of matrix rows.
The second line contains m - the number of columns, m and n do not exceed 1000. The next n lines contain a matrix. The numbers in it do not exceed modulo 1000.

**Print the transposed matrix in the same format as given in the input. Each row of the matrix is printed on a separate line, the elements are separated by spaces.**

## B. To-Do List
Vasya needs to print out his to-do list for today. 
Help him and write a function that prints all his to-dos. 
We know that Vasya has no more than 5000 things to do.

**The function must print the list items one per line.**

## C. Unloved business:
Vasya ponders what not to do from the list. 
But all the items seem to be very important! 
Vasya decides to puzzle out a number and delete the thing that goes under that number. 
The to-do list is represented as a single-connected list. 

**Write a solution function that takes as input the head of the list**
**and the number of the deleted case and returns the head of the updated list.**

## D. Caring Mom.
Vasya's mother wants to know what her son plans to do and when. 
Help her: write a function solution that determines the index of the first occurrence 
of the value passed to it as input in the linked list, if the value is present.

The function takes as input the head of a single-connected list and the element, 
to be found.

**The function returns the index of the first occurrence of the element sought**
in the list (indexing starts from zero). 
If the element is not found, you have to return -1. 

## E. It's the other way around:
Vasya decided to confuse his mother -- to do things in reverse order. 
His to-do list is now stored in a double-connected list. 
Write a function that returns the list in reverse order.

The function takes as input a single argument -- the head of the double-connected list.

**The function should return the head of the expanded list.**

## F. Stack - Max
We need to implement a StackMax class that supports the operation of determining 
maximum among all elements in the stack. The class must also support 
all operations implemented in the Stack class from the lesson. 
No more than three methods can be implemented in the StackMax class.

The stack can only contain data of the types that support the comparison operation. 
Otherwise the maximal search operation will be incorrect.

The first line contains one number n - the number of commands. 
n does not exceed 1000. The next n lines contain commands. 
Commands can be of the following kinds:
push x - add number x to the stack
pop - remove number from the stack top
get_max - print the maximum number in the stack


For each get_max command, print the result of its execution. 
If the stack is empty, print None for get_max command. 
If deletion from an empty stack occurs, print error. 

## G. Stack - MaxEffective.

Implement the StackMaxEffective class that supports the operation of determining 
maximum among the elements in the stack. The complexity of the operation should be O(1). 
For an empty stack, the operation should return None. 
The push and pop must also be performed in a constant time.

The first line contains one number - the number of instructions, 
It doesn't exceed 1000. Next are commands, one per line. 
Commands may be of the following kinds:
push x - add number x to the stack
pop - remove number from the stack top
get_max - print the maximal number in the stack

For each get_max command, print the result of its execution. 
If the stack is empty, print None for get_max command. 
If an empty stack is deleted, print error.

## H. Stack Sequence
This is the task Timofey offered at a job interview to one of the candidates. 
If you haven't encountered it yet, you probably will - it's quite 
popular.

A bracket sequence is given. You need to determine if it is correct.
Let's stick to this definition:
- an empty string is a valid bracket sequence;
- a valid parentheses sequence, 
taken in brackets of the same type is a correct bracket sequence;
- correct bracket sequence with brackets taken from the left or from the right 
The correct bracket sequence taken from the left or right side is also the correct bracket sequence.

The input is a sequence of three kinds of brackets: [], (), {}.

Write an is_correct_bracket_seq function that takes as input 
bracket sequence and returns True, 
if the sequence is correct, otherwise False.

The input is a single string containing the bracket sequence.


## I. Limited Queue
Next, Timothy needs to write a class called MyQueueSized(), 
that takes the max_size parameter, which means the maximum allowed 
number of elements in the queue.

The first line contains one number - the number of commands, it doesn't exceed 5000. 
The second line contains the maximal allowed queue size, 
It does not exceed 5000. Next are the commands, one per line. 
Commands can be of the following types:
push x - add number x to the queue
pop - remove numbers from the queue and print them.
peek - print the first number in the queue
size - return the queue size

If the permissible queue size is exceeded "error" should be output. 
When calling the pop operation for an empty queue it should return None.


## J. List queue
Timothy's favorite version of the queue is the queue, 
Timofey's favorite queue is the one written using a linked list. 
Help him with the implementation. The queue should support get, put, size methods.

The first line contains the number of commands n - an integer not exceeding 1000.
Each of the following n lines contains a command: get, put, or size.

When the get method is called, print the return value. 
If the get method is called on an empty queue, print 'error'. 
When the size method is called, print the size of the queue.

# Final tasks
https://contest.yandex.ru/contest/23759/problems/

## A. Dek
Gosha decided to implement a data structure Dec, whose maximum size 
which is defined by a given number. 
The push_back, push_front, pop_front, pop_back methods worked correctly. 
But if the deck had a lot of elements, the program took a very long time. 
The point is that not all operations were performed for O(1). 
Help Gosha! Write an efficient implementation.

The first line contains the number of commands n - an integer not exceeding 5000. 
The second line contains number m, the maximum size of the stack. 
It does not exceed 1000. 
The next n lines contain one of the commands:
push_back value
push_front value
pop_front
pop_back
value is an integer which modulo does not exceed 1000.

When calling the pop_front and pop_back commands you should print the return value. 
If they are called for an empty stack, print 'error'. 
If the push_back or push_front command is called for a stack 
is equal to the maximum possible size, print 'error' too.

## B. Calculator

The assignment is related to reverse polish notation. It is used for parsing arithmetic expressions. Compared to the other method used for this problem, using an operation tree, it is more compact because it does not use brackets. It is also sometimes called postfix notation.

In postfix notation, the operands are in front of the operation signs.

Example 1:  
3 4 +  
will equal 7, and means 3 + 4

Example 2:  
10 2 4 * -  
equals 2, which means 10 - 2 * 4

Let's look at the last example more closely:

The sign * is right after the numbers 2 and 4, so you have to apply to them the operation that this sign denotes, that is, multiply these two numbers. The result is 8.

The expression will then take the form:

10 8 -

The minus operation should be applied to the two numbers preceding it, that is, 10 and 8. The result is 2.

Let's analyze the algorithm in details. We will use the stack to implement it.

To calculate the value of an expression written in inverse Polish notation, the expression has to be read from left to right, and the following steps have to be followed:

If an operand is given at the input, it is placed on the top of the stack. - If an operation sign is given as input, it is executed over the required number of values from the stack, taken in order of addition. The result of the operation is placed at the top of the stack. 
2. If the input character set is not completely processed, go to step 1. 
3. After the input character set is completely processed, the result of the expression calculation is placed at the top of the stack.


### Input format.
The only line contains an expression written in inverse Polish notation. Numbers and arithmetic operations are separated by spaces.

The input can contain operations: +, -, *, / and numbers up to 10000 modulo.

It is guaranteed that the value of intermediate expressions in the test data modulo does not exceed 50000.

### Output format. 
The only number is the value of the expression.
