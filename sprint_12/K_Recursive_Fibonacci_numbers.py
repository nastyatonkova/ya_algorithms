"""
Timothy had n (0≤n≤32) interns. Each trainee wanted to be better than his predecessors, 
so the i-th trainee made as many commits as the previous two trainees made in total. 
The first two interns were less proactive - they each made one commit.

Let Fi be the number of commits made by the i-th trainee (trainees are numbered from zero). 
Then the following holds: F0=F1=1. For all i≥2, Fi=Fi-1+Fi-2 is satisfied.

Determine how much code the next trainee will write -- find Fn.

The solution must be implemented recursively. 
"""


n = int(input()) + 1
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(n))
