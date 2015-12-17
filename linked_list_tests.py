from linked_list.linked_list import Node, LinkedList
import unittest


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.second_linked_list = LinkedList()

        # for search and delete test
        self.second_linked_list.insert("Batman")
        self.second_linked_list.insert("Superman")
        self.second_linked_list.insert("Deadpool")

    def test_insert(self):
        self.linked_list.insert("Matheus")

        self.assertEqual(self.linked_list.head.get_data(), "Matheus")
        self.assertEqual(self.linked_list.head.get_next(), None)

    def test_search(self):
        node = self.second_linked_list.search("Superman")

        self.assertNotEqual(node, None)
        self.assertEqual(node.get_data(), "Superman")

    def test_delete(self):
        self.second_linked_list.delete("Deadpool")
        self.assertEqual(self.second_linked_list.head.get_data(), "Superman")

        self.second_linked_list.delete("Superman")
        self.assertEqual(self.second_linked_list.head.get_next(), None)

if __name__ == '__main__':
    unittest.main()