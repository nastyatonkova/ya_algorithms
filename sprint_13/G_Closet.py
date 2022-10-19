"""
Rita decided to keep only three colors of clothes: pink, yellow, and crimson. 
After the other colors were put away, Rita wanted to sort her new closet by color. 
First should go pink, then yellow, and finally crimson. Help Rita with this task.

Note: try to solve the problem in one pass over the array! 
"""


def counting_sort():
    n = int(input())
    things = list(map(int, input().strip().split()))
    list_0 = []
    list_1 = []
    list_2 = []
    for thing in things:
        if thing == 0:
            list_0.append("0")
        elif thing == 1:
            list_1.append("1")
        else:
            list_2.append("2")

    print(" ".join(list_0 + list_1 + list_2))


if __name__ == '__main__':
    counting_sort()
