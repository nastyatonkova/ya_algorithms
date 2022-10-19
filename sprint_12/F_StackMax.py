"""
We need to implement a StackMax class that supports 
the operation of determining the maximum among all elements 
in the stack. The class must support push(x) where x is an integer, 
pop() and get_max() operations.

"""


class StackMax:
    def __init__(self):
        self.items = []
        self.max = 0
        
    def is_empty(self):
        return self.items==[]
    
    def get_size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            return 'error'
        return self.items.pop()
    
    def print_stack(self):
        return self.items

    def get_max(self):
        if self.is_empty():
            return 'None'
        return int(max(map(float, self.items)))

s = StackMax()
n = int(input())
result = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        s.push(command[1])
    if command[0] == 'pop':
        if s.pop() == 'error':
            result.append('error')
    if command[0] == 'get_max':
        result.append(s.get_max())
for i in result:
    print(i)
