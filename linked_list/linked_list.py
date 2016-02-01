"""
    linked_list.py
    Implements a Linked List.
"""

class Node(object):
    """
    This class represents a node in the linked list
    """
    def __init__(self, data=None, node=None):
        self.data = data
        self.next = node

    def get_data(self):
        """
        Returns the node's data
        """
        return self.data

    def get_next(self):
        """
        Return the next node
        """
        return self.next

    def set_next(self, node):
        """
        Sets the next node
        """
        self.next = node


class LinkedList(object):
    """
    Class that implements a linked list
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """
        Insert data at the beginning of the linked list
        """
        node = Node(data)
        node.set_next(self.head)

        self.head = node

    def insert_at_tail(self, data):
        """
        Insert data at the end of the linked list
        """
        if self.head is None:
            self.insert(data)
        else:
            node = self.head

            while node.get_next():
                node = node.get_next()

            node.set_next(Node(data))

    def size(self):
        """
        Returns the size of the linked list
        """
        size = 0
        current_node = self.head

        while current_node:
            size += 1
            current_node = current_node.get_next()

        return size

    def search(self, data):
        """
        Search for data in the linked list
        """
        current_node = self.head
        found = False

        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next()

        if current_node is None:
            raise ValueError('Data not found.')

        return current_node

    def delete(self, data):
        """
        Deletes a node from the linked list
        """
        current_node = self.head
        previous_node = None
        found = False

        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if current_node is None:
            raise ValueError('Data not found.')

        if previous_node is None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())

    def show(self):
        """
        Prints the linked list
        """
        current_node = self.head
        nodes = []

        while current_node:
            nodes.append(current_node.get_data())
            current_node = current_node.get_next()

        return " => ".join(map(str, nodes))
