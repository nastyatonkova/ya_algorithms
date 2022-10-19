"""
Vasya's classmates came to visit. His mother decided to treat the boys with cookies.
But it's not that easy. Cookies can be different sizes. 
And each child has a greedy factor - the minimum size of a cookie he will take. 
You have to figure out how many kids will be satisfied at best when they act optimally.
Each child can take no more than one cookie.  
"""


def solution(children, cookies):
    children.sort()
    cookies.sort()

    i = len(children) - 1
    j = len(cookies) - 1
    count = 0

    while j >= 0 and i >= 0:
        if cookies[j] >= children[i]:
            cookies.pop(j)
            children.pop(i)
            j -= 1
            count += 1
        i -= 1
    return count

num_children = input()
children = list(map(int, (input().split())))
num_cookies = input()
cookies = list(map(int, (input().split())))

print(solution(children, cookies))
