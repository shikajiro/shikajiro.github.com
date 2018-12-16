#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITETITLE = "VS Resistance"
SITESUBTITLE = "Android App Programmer"

AUTHOR = 'shikajiro'
SITELOGO = "/images/shikajiro.jpg"
SITENAME = 'VS Resistance'
SITEURL = '/'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Profile', '/profile'),)

MAIN_MENU = True
MENUITEMS = (
('archives','/archives'),
('categories','/categories'),
('tags','/tags'),
)

# Social widget
SOCIAL = (('github', 'https://github.com/shikajiro'),
          ('twitter', 'https://twitter.com/shikajiro'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/Users/shikajiro/Develop/pelican-themes/Flex"

# PLUGIN_PATHS = ["/Users/shikajiro/Documents/pelican-plugins"]
PLUGINS = ["pelican_gist"]

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

GOOGLE_ANALYTICS = "UA-389036-10"