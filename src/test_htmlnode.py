import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(
            "p",
            "Hello, world!",
        )

        node2 = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )

    if __name__ == "__main__":
        unittest.main()


class TestParentNode(unittest.TestCase):
    def test_result(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print(node)


