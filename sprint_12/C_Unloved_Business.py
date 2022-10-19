"""
Vasya ponders what he might not do on the to-do list he has made. 
But all the items seem to be very important! Vasya decides to puzzle out a number and delete 
the thing that goes under that number. The to-do list is represented as a single-connected list. 
Write a solution function that takes as input the head of the list and the number of the deleted 
to-do list and returns the head of the updated list. 

Note: in this problem you don't need to read the input data. 
The only thing you need to write is a function that takes the list head 
as input and prints its elements. Below is a description of the structure 
that specifies the node of the list.

"""


# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        head = node.next_item
        return head
    else:
        head = node
    while idx-1:
        if node.next_item is not None:
            node = node.next_item
        else:
            return head
        idx -= 1
    node.next_item = node.next_item.next_item
    return head
    
def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3

if __name__ == '__main__':
    test()
    