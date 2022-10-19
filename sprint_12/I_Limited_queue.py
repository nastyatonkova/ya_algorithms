"""
Astrologers has declared a day of limited-size queues. 
Timothy needs to write a class called MyQueueSized that takes the max_size parameter, 
which means the maximum number of elements allowed in the queue.

Help him out by implementing a program that will emulate such a queue. 
The functions to support are described in the input format.

"""


class MyQueueSized:

    def __init__(self, max_size):
        self.queue = [None for _ in range(n)]
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
  
    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return 'OK'
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x 

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


n = int(input())
queue_length = int(input())
q = MyQueueSized(queue_length)

result = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        a = q.push(command[1])
        if a == 'error':
            result.append(a) 
    if command[0] == 'pop':
        result.append(q.pop())
    if command[0] == 'peek':
        result.append(q.peek())
        
    if command[0] == 'size':
        result.append(q.size)
for x in result:
    print(x)
