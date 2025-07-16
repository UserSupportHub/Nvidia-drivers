# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Nvidia Driver Installation Guide'
copyright = '2025, YourCompanyName'
author = 'YourCompanyName Tech Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output -------------------------------------------------------------

# Choose your HTML theme (most popular: sphinx_rtd_theme)
# To use this theme, run: pip install sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'

# Custom HTML title
html_title = "How to Download and Install Nvidia Drivers"

# Short title (shown in navigation)
html_short_title = "Nvidia Driver Help"

# Favicon (optional - place favicon.ico in _static folder)
html_favicon = 'favicon.ico'

# Hide "View page source" in the top right
html_show_sourcelink = False

# Allow raw HTML inside .rst files
html_allow_unsafe = True

# Theme options (optional - depends on theme)
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'style_external_links': True,
}

# Static files (custom CSS, JS, images)
# Uncomment if needed and create a _static folder
# html_static_path = ['_static']

# -- Custom Scripts or Styles (Optional) -------------------------------------

# def setup(app):
#     app.add_css_file("custom.css")
#     app.add_js_file("custom.js")
