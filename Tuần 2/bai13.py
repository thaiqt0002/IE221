class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = None
        self.addHead(data)

    def is_empty(self):
        return self.head is None

    def addHead(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addTail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        if self.is_empty():
            print("LinkedList is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

list = LinkedList(4)
list.addHead(2)
list.addHead(3)
list.addHead(4)
list.addHead(5)
list.addHead(2)
list.addTail(7)
list.addTail(1)
list.addTail(4)
list.addTail(6)
list.addTail(8)
list.display()
