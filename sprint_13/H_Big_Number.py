"""
In the evening the children decided to play the game "Big Number".
The numbers are given. You need to find out what is the biggest number you can make out of them. 
"""


def bubble_sort(number, source_array):
    for i in range(number - 1):
        for j in range(0, number-i-1):
            var1 = source_array[j] + source_array[j+1]
            var2 = source_array[j+1] + source_array[j]
            if var1 < var2:
                source_array[j], source_array[j+1] = source_array[j+1], source_array[j]
                
    print("".join(source_array))
if __name__ == '__main__':
    number = int(input())
    source_array = input().split(' ')
    bubble_sort(number, source_array)
