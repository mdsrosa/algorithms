from linked_list.linked_list import Node, LinkedList
import unittest


class LinkedListTest(unittest.TestCase):
    def test_insert(self):
        linked_list = LinkedList()
        linked_list.insert("Matheus")

        self.assertEqual(linked_list.head.get_data(), "Matheus")
        self.assertEqual(linked_list.head.get_next(), None)

    def test_search(self):
        linked_list = LinkedList()

        linked_list.insert("Batman")
        linked_list.insert("Superman")
        linked_list.insert("Deadpool")

        node = linked_list.search("Superman")

        self.assertNotEqual(node, None)
        self.assertEqual(node.get_data(), "Superman")

    def test_delete(self):
        linked_list = LinkedList()

        linked_list.insert("Darth Vader")
        linked_list.insert("R2-D2")
        linked_list.insert("Luke Skywalker")

        linked_list.delete("Luke Skywalker")
        self.assertEqual(linked_list.head.get_data(), "R2-D2")

        linked_list.delete("R2-D2")
        self.assertEqual(linked_list.head.get_next(), None)

    def test_insert_two_items(self):
        linked_list = LinkedList()

        linked_list.insert("Ironman")
        linked_list.insert("Captain America")

        self.assertEqual(linked_list.head.get_data(), "Captain America")

        next_head = linked_list.head.get_next()

        self.assertEqual(next_head.get_data(), "Ironman")


if __name__ == '__main__':
    unittest.main()