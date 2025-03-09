import unittest
from textnode import *
from htmlnode import *
from inline_markdown import *
from copystatic import *


from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        exp = [('rick roll','https://i.imgur.com/aKaOqIh.gif'), ('obi wan','https://i.imgur.com/fJRm4Vk.jpeg')]
        res = extract_markdown_images(text)
        self.assertListEqual(res,exp)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        exp = [('to boot dev','https://www.boot.dev'), ('to youtube','https://www.youtube.com/@bootdotdev')]
        res = extract_markdown_links(text)
        self.assertListEqual(res,exp)

    def test_split_nodes_image(self):
        old_nodes = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)]
        new_nodes =  split_nodes_image(old_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT), 
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), 
                TextNode(" and ", TextType.TEXT), 
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
            ],
            new_nodes,
        )

    def test_split_nodes_link(self):
        old_nodes = [TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)]
        new_nodes =  split_nodes_link(old_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT), 
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"), 
                TextNode(" and ", TextType.TEXT), 
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"), 
            ],
            new_nodes,
        )


    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
                [
                    TextNode("This is ", TextType.TEXT), 
                    TextNode("text", TextType.BOLD), 
                    TextNode(" with an ", TextType.TEXT), 
                    TextNode("italic", TextType.ITALIC), 
                    TextNode(" word and a ", TextType.TEXT), 
                    TextNode("code block", TextType.CODE), 
                    TextNode(" and an ", TextType.TEXT), 
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
                    TextNode(" and a ", TextType.TEXT), 
                    TextNode("link", TextType.LINK, "https://boot.dev")
                ]
            )



if __name__ == "__main__":
    unittest.main()
