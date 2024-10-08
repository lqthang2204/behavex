# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'BehaveX'
copyright = '2023, hrcorval'
author = 'hrcorval'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# The master toctree document.
master_doc = 'index'

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# -- MyST Parser configuration -----------------------------------------------
myst_enable_extensions = [
    "colon_fence",
]

# -- Setup for markdown files ------------------------------------------------
import commonmark


def setup(app):
    app.connect('source-read', process_markdown)

def process_markdown(app, docname, source):
    if docname == 'index':
        with open('../README.md', 'r') as f:
            markdown_content = f.read()
        parser = commonmark.Parser()
        ast = parser.parse(markdown_content)
        renderer = commonmark.HtmlRenderer()
        html = renderer.render(ast)
        source[0] = html
