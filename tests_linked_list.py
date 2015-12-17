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

    def test_search_unexistent_item(self):
        linked_list = LinkedList()

        linked_list.insert("Spiderman")
        linked_list.insert("Hulk")

        with self.assertRaises(ValueError):
            node_found = linked_list.search("Daredevil")

    def test_search_in_empty_list(self):
        linked_list = LinkedList()

        with self.assertRaises(ValueError):
            linked_list.search("Oliver Queen")

    def test_delete(self):
        linked_list = LinkedList()

        linked_list.insert("Darth Vader")
        linked_list.insert("R2-D2")
        linked_list.insert("Luke Skywalker")

        linked_list.delete("Luke Skywalker")
        self.assertEqual(linked_list.head.get_data(), "R2-D2")

        linked_list.delete("R2-D2")
        self.assertEqual(linked_list.head.get_next(), None)

    def test_delete_unexistent_item(self):
        linked_list = LinkedList()

        linked_list.insert("Flash")
        linked_list.insert("Arrow")

        with self.assertRaises(ValueError):
            linked_list.delete("Harrison Wells")

    def test_delete_empty_list(self):
        linked_list = LinkedList()

        with self.assertRaises(ValueError):
            linked_list.delete("Barry Allen")

    def test_delete_next_and_reassignment(self):
        linked_list = LinkedList()

        linked_list.insert("Tony Stark")
        linked_list.insert("Thor")
        linked_list.insert("Bruce Banner")
        linked_list.insert("Clint Barton")

        linked_list.delete("Clint Barton")
        linked_list.delete("Thor")

        self.assertEqual(linked_list.head.get_data(), "Bruce Banner")

    def test_insert_two_items(self):
        linked_list = LinkedList()

        linked_list.insert("Ironman")
        linked_list.insert("Captain America")

        self.assertEqual(linked_list.head.get_data(), "Captain America")

        next_head = linked_list.head.get_next()

        self.assertEqual(next_head.get_data(), "Ironman")

    def test_next_node(self):
        linked_list = LinkedList()

        linked_list.insert("Clark Kent")
        linked_list.insert("Bruce Wayne")
        linked_list.insert("Peter Parker")

        self.assertEqual(linked_list.head.get_data(), "Peter Parker")
        next_head = linked_list.head.get_next()
        self.assertEqual(next_head.get_data(), "Bruce Wayne")
        last_node = next_head.get_next()
        self.assertEqual(last_node.get_data(), "Clark Kent")

    def test_show(self):
        linked_list = LinkedList()

        linked_list.insert("Aquaman")
        linked_list.insert("Wonder Woman")
        linked_list.insert("Green Lantern")

        expected = "Green Lantern => Wonder Woman => Aquaman"

        self.assertEqual(linked_list.show(), expected)

if __name__ == '__main__':
    unittest.main()
