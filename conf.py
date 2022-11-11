# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ZEISS Industry Quality Solutions'
copyright = '2022, Carl Zeiss GOM Metrology GmbH'
author = 'Carl Zeiss GOM Metrology GmbH'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_rtd_theme', 'sphinx-favicon']
source_suffix = ['.rst', '.md']
exclude_patterns = ['README.md']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]  # html_static_path is required if you use the "static-file" parameter

favicons = [
    {
        "rel": "icon",
        "sizes": "16x16",
        "static-file": "favicon.png",  # => use `_static/favicon.png`
        "type": "image/png",
    }
]
