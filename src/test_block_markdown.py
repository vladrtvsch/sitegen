import unittest
from block_markdown import *

class TestInlineMarkdown(unittest.TestCase):

	def test_markdown_to_blocks(self):
		text = " #Hello world\n\n This is a paragraph"
		blocks = markdown_to_blocks(text)
		self.assertListEqual(
			blocks,
			['#Hello world','This is a paragraph']
			)

	def test_block_to_block_type(self):
		md ="""1. This is **bolded** paragraph
2. This is another paragraph with *italic* text and `code` here
3. This is the same paragraph on a new line
4. This is a list
5. with items"""
		block_type = block_to_block_type(md)
		self.assertEqual(block_type, BlockType.OLIST)

	def test_markdown_to_html_node(self):
		md ="""## Hello Workd

		Simple Paragraph"""		
		node = markdown_to_html_node(md)
		self.assertEqual(node.__repr__(),
			"ParentNode(div, children: [ParentNode(h2, children: [LeafNode(None, Hello Workd, None)], None), ParentNode(p, children: [LeafNode(None, Simple Paragraph, None)], None)], None)")

	def test_extract_title(self):
		text = "# Hello"
		title = extract_title(text)
		self.assertEqual(title, 'Hello')


if __name__ == "__main__":
    unittest.main()