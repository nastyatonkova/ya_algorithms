"""
Implement the StackMaxEffective class that supports the operation to determine 
the maximum among the elements in the stack. 
The complexity of the operation must be O(1). 
For an empty stack, the operation should return None. 
Push(x) and pop() should also be performed in constant time. 

"""


class StackMaxEffective:

    def __init__(self):
        self.items = []
        self.max = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[len(self.items)-1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[len(self.items)-1])
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        self.max.pop()
        return self.items.pop()

    def get_max(self):
        if self.is_empty():
            return 'None'
        return self.max[len(self.items) - 1]

    def print_stack(self):
        return self.items
    
    def print_maxes(self):
        return self.max


s = StackMaxEffective()
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
