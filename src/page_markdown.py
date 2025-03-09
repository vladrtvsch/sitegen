from block_markdown import *
from htmlnode import *
import os
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	file = open(from_path,"r")
	file_content = file.read()
	template = open(template_path, "r")
	template_content = template.read()

	content_node = markdown_to_html_node(file_content)

	content_html = content_node.to_html()

	title = extract_title(file_content)

	page_html = template_content.replace('{{ Title }}', title)
	page_html = page_html.replace('{{ Content }}', content_html)

	dirname = os.path.dirname(dest_path)
	os.makedirs(dirname,exist_ok=True)

	file = open(dest_path, "w")
	file.write(page_html)
	file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
