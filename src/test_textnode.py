import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_text_nt_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertEqual(node.text_type, node2.text_type)
        self.assertNotEqual(node.text, node2.text)

    def test_text_type_nt_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node.text, node2.text)
        self.assertNotEqual(node.text_type, node2.text_type)

    if __name__ == "__main__":
        unittest.main()
