"""
Vasya's mother wants to know what her son plans to do and when. 
Help her: write a solution function that determines the index of the first 
occurrence of the value passed to it in the linked list, if the value is present.

Note: in this problem you don't need to read the input data. 
We only need to write a function that takes as input the head of the list 
and the item to be found, and returns an integer - the index of the found item or -1. 

"""


# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item

def solution(head, value):
    node = head
    index = 0
    while node:
        if node.value == value:
            return index
        index += 1
        node = node.next_item
    return -1

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2

if __name__ == '__main__':
    test()
    