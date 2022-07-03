project = 'Akinbowale Akin-Taylor'
copyright = '2022, Akinbowale Akin-Taylor <a@akintaylor.com>'
author = 'Akinbowale Akin-Taylor <a@akintaylor.com>'

extensions = [
    'myst_parser',
    'ablog',
    'sphinx.ext.intersphinx',
    'sphinx_panels'
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/akintaylor",
  "twitter_url": "https://twitter.com/theakintaylor",
}

html_static_path = ['_static']
