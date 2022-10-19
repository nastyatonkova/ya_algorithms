"""
Gosha implemented a data structure Dec, whose maximum size is defined by a given number. 
The methods push_back(x), push_front(x), pop_back(), pop_front() worked correctly. 
But if there were a lot of items in the deck, the program took a very long time. 
The thing is, not all operations were performed for O(1). Help Gosha! Write an efficient implementation.

Note: when implementing, use a ring buffer.


Class Dek consists of the following attributes:
self.elements - circular buffer to store values
self.max_size - max size of buffer
self.head - position of first element
self.tail - position of last element
self.count - number of elements

and following methods:

push_back
inserts element at back of the deque (double-ended queue)
- it checks if buffer is full than raises OverflowError, otherwise
- inserts value into <elements> array with index=<tail>
- increases value of the tail field by 1 and takes modulo max_size
  (this is done to ensure that the first cell follows the last one)
- increases <count> by 1

push_front
inserts element at front of the deque
- it checks if buffer is full than raises OverflowError, otherwise
- inserts value into <elements> array with index=<head-1>
- decreases value of the head field by 1 and takes modulo max_size
- increases <count> by 1

pop_back
removes last element of the deque
- it checks if buffer is empty than raises IndexError, otherwise
- returns value of the element with index=<tail-1>
- inserts None to the element with index=<tail-1>
- decreases value of the tail field by 1 and takes modulo max_size
- decreases <count> by 1

pop_front
removes first element of the deque
- it checks if buffer is empty than raises IndexError, otherwise
- returns value of the element with index=<head+1>
- inserts None to the element with index=<head+1>
- increases value of the head field by 1 and takes modulo max_size
- decreases <count> by 1
"""


from typing import List, Tuple, NoReturn


class Dek:

    def __init__(self, max_size: int):
        self.__elements = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__count = 0

    def is_empty(self):
        return self.__count == 0

    def push_back(self, value: int):
        if self.__count == self.__max_size:
            raise OverflowError
        self.__elements[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__count += 1


    def push_front(self, value: int):
        if self.__count == self.__max_size:
            raise OverflowError
        self.__elements[self.__head - 1] = value
        self.__head = (self.__head - 1) % self.__max_size
        self.__count += 1


    def pop_back(self):
        if self.is_empty():
            raise IndexError
        x = self.__elements[self.__tail - 1]
        self.__elements[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__count -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        x = self.__elements[self.__head]
        self.__elements[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__count -= 1
        return x


def solution() -> NoReturn:
    count_command = int(input())
    dek_len = int(input())

    dek = Dek(dek_len)
    for _ in range(count_command):
        command, *values = input().split()
        operation = getattr(dek, command)
        values = tuple(map(int, values))
        try:
            result = operation(*values)
        except (IndexError, OverflowError):
            result = 'error'
        if result is not None:
            print(result)


if __name__ == '__main__':
    solution()
