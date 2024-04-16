import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.path.append(os.path.abspath('../../../jobject'))
sys.path.append(os.path.abspath('../../../jsonb'))
sys.path.append(os.path.abspath('../../../tools'))
sys.path.append(os.path.abspath('../../../undefined'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ouroboros Define'
copyright = '2024, Ouroboros Coding Inc.'
author = 'Ouroboros Coding Inc.'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
