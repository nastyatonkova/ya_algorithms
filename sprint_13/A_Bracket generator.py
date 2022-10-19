"""

Rita, on Timothy's errand, is putting in order the correct parentheses sequences (PSPs) 
consisting only of parentheses (). 
To do this, she needs to generate all PSPs of length 2n in alphabetical order -- 
the alphabet consists of ( and ) and the opening bracket comes before the closing one.

Help Rita -- write a program which, given n, will print all the PSPs in the right order.

Consider the second example. You're going to print a PSP of four characters. There are only two of them:

    (())
    ()()

(()) comes before ()(), because their first character is the same, 
and the second position has (, which comes before ).  
"""


def gen_binary(control, n1, n2, prefix):
    if n1 == 0 and n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            gen_binary(control + 1, n1 - 1, n2, prefix + '(')
        if (control > 0 and n2 > 0):
            gen_binary(control - 1, n1, n2 - 1, prefix + ')')

n = int(input())
control = 0
n1 = n
n2 = n
gen_binary(control, n1, n2, '') 
