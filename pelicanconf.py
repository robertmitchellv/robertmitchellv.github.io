#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site-info
AUTHOR = 'Robert B. Mitchell V'

SITENAME = 'rbmv // critical data, info, + analysis'
SITEURL = 'http://robertmitchellv.com'

PATH = 'content'
STATIC_PATHS = ['images', 'pages']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Theme + look of site 
THEME = 'my-theme/'                                     
BOOTSTRAP_THEME = 'yeti'

CUSTOM_CSS = 'theme/css/custom.css'
BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css'
BS3_JS = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js'
BS3_THEME = 'http://bootswatch.com/flatly/bootstrap.min.css'

PYGMENTS_STYLE = 'monokai'

DISPLAY_CATEGORIES_ON_MENU = False

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))

HIDE_SIDEBAR = True

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search']

# Site Brand
SITELOGO = 'images/rbmv_curve.png'
SITELOGO_SIZE = 130
HIDE_SITENAME = True
AVATAR = 'images/me.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('GitHub', 'http://github.com/robertmitchellv'),
          ('Twitter', 'http://twitter.com/RobertMitchellV'),
          ('LinkedIn', 'http://www.linkedin.com/in/robertmitchellv'),)

GITHUB_USER = 'robertmitchellv'
GITHUB_SKIP_FORK = True

TWITTER_USERNAME = 'RobertMitchellV'

DEFAULT_PAGINATION = 4

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAG_URL = 'tags.html'

