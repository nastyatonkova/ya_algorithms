"""
Vasya decided to save money for two identical bicycles - for himself and his sister. 
Vasya has a piggy bank into which he can add money every day (if he is financially able to do so, 
of course). In the process of saving he does not take money out of the piggy bank.

You have information about the growth of Vasya's savings - how much money he has in the piggy bank on each of the days.

Your task is to determine the value of the bike

    the first day on which Vasya could buy one bicycle,
    and the first day on which Vasya could buy two bikes.

Hint: the solution should work for O(log n).  
"""


def binarySearch(money, price, left, right):
    if (right <= left and left != 0):
        return -1
    middle = (left + right) // 2
    if (money[middle] >= price and (money[middle - 1] < price or middle == 0)):
        return middle + 1
    elif price <= money[middle]:
        return binarySearch(money, price, left, middle)
    else:
        return binarySearch(money, price, middle + 1, right)
days = int(input())
money = [int(num) for num in input().split(' ')]
price = int(input())

print(binarySearch(money, price, left = 0, right = len(money)), end=' ')
print(binarySearch(money, price * 2, left = 0, right = len(money)), end=' ')
