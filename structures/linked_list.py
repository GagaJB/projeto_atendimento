class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, id_cliente):
        curr = self.head
        prev = None
        while curr and curr.data.id_cliente != id_cliente:
            prev = curr
            curr = curr.next
        if not curr:
            return False
        if not prev:
            self.head = curr.next
        else:
            prev.next = curr.next
        return True

    def get_all(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements