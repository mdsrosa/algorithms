from linked_list.linked_list import Node, LinkedList
import unittest


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.second_linked_list = LinkedList()

        self.second_linked_list.insert("Batman")
        self.second_linked_list.insert("Superman")
        self.second_linked_list.insert("Deadpool")

    def test_insert(self):
        self.linked_list.insert("Matheus")

        self.assertEqual(self.linked_list.head.get_data(), "Matheus")
        self.assertEqual(self.linked_list.head.get_next_node(), None)

if __name__ == '__main__':
    unittest.main()