# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Base-Conversion-Kit'
copyright = '2023, Pavlos Orfanidis'
author = 'Pavlos Orfanidis'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ['_static']
master_doc = 'index'
# conf.py


html_theme_options = {
    'logo': 'logo.jpg',
    'description': 'base-conversion-kit: Perform operations with numbers in different bases',
    'github_user': 'porfanid',
    'github_repo': 'base-conversion-kit',
    'github_banner': True,
    'github_button': True,


    'travis_button': False,
    'codecov_button': True,
    'sidebar_includehidden': True,
    'show_related': False,
    'donate_url': 'https://ko-fi.com/porfanid',
    'show_powered_by': False,

}


html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        #'searchbox.html',
        'donate.html',
    ]
}
