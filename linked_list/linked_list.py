class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        node = Node(data)
        node.set_next(self.head)

        self.head = node

    def size(self):
        size = 0
        current_node = self.head

        while current_node:
            size += 1
            current_node = current_node.get_next()

        return size