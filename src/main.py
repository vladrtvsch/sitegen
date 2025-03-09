from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *
from copystatic import *
from page_markdown import *
import os


copy_files_recursive('./static','./public',True)

# generate_page('./content/index.md', './template.html', './public/index.html')

generate_pages_recursive('./content','./template.html', './public/')