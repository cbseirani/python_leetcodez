'''
 * A singly linked list is a linear data structure where each
 *  element (node) contains a value and a reference (link) to the
 *  next node in the sequence, forming a chain-like collection.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def insert(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self._head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("null")
    