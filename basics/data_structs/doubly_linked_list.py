'''
A doubly linked list is a linear data structure where each node
    contains a reference to both the next and the previous node, 
    allowing traversal in both directions.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
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
            new_node.previous = current
            current.next = new_node

    def display_forward_traversal(self):
        current = self._head
        while current is not None:
            print(current.data, end = " -> ")
            current = current.next
        print("null")

    def display_reverse_traversal(self):
        current = self._head
        if not current:  # Check if the list is empty
            print("null")
            return

        # traverse to the end
        while current.next is not None:
            current = current.next

        # traverse backward and print
        while current is not None:
            print(current.data, end = " <- ")
            current = current.previous
        print("null")