"""
Vasya needs to print out his to-do list for today. 
Help him: write a function that prints out all his to-dos. 
We know that Vasya has no more than 5000 things to do.

Note: in this problem you don't need to read the input data. 
The only thing you need to write is a function that takes the list head 
as input and prints its elements. Below is a description of the structure 
that specifies the node of the list.

"""


LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node):
    while node:
        print(node.value)
        node = node.next_item


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()
    