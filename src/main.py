from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *
from copystatic import *
from page_markdown import *
import os
import sys

basepath = '/'

if len(sys.argv)>1:
	basepath = sys.argv[1]

print(f'BSP:{basepath}')

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

copy_files_recursive(dir_path_static,dir_path_public,True)

# generate_page('./content/index.md', './template.html', './public/index.html')

generate_pages_recursive(dir_path_content,template_path, dir_path_public,basepath)