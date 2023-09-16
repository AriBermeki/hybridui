# conf.py

import os
import sys
import sphinx_rtd_theme

# Add your project directory to the Python path
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'Hybrid'
author = 'Ari Bermeki'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
master_doc = 'index'

# Add any extensions you need
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

# Specify the location of source code
# For example, if your source code is in a 'src' directory
# you can use the following line:
# source_dir = os.path.abspath('../src')

# General configuration
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Add any custom settings here

# HTML settings
html_static_path = ['_static']
