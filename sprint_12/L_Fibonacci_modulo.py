"""


Timothy had very many interns, as many as N (0 ≤ N ≤ 106) people. 
Each trainee wanted to be better than his predecessors, so the i-th trainee made as many commits 
as the previous two trainees made in total. The first two interns were less proactive - they each made one commit.

Let Fi be the number of commits made by the i-th trainee (trainees are numbered from zero). 
The first two trainees each made one commit: F0=F1=1. For all i≥ 2, Fi=Fi-1+Fi-2 is executed.

Determine how much code the next trainee will write -- find the last k digits of the number Fn.


How to find the last k digits

To calculate the last k digits of some number x, just take the remainder of its division 
by the number 10k. This operation is denoted as x mod 10k. 
Find out how the operation of taking the remainder modulo is written in your programming language.

Also pay attention to possible integer type overflow, if this happens in your language.
"""


n, k = (int(i) for i in input().split())


def fib_last_digit(n, k):
    d = (10 ** k)
    fib1 = fib2 = 1

    while n > 0:
        fib1, fib2 = fib2, (fib1 + fib2) % d
        n -= 1

    return fib1 

print (fib_last_digit(n, k))
