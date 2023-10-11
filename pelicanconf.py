#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITETITLE = "shikajiro blog"
SITESUBTITLE = "Freelance FullStack Programmer"

AUTHOR = 'shikajiro'
SITELOGO = "/images/shikajiro-icon.png"
SITENAME = 'shikajiro blog'
SITEURL = 'https://shikajiro.github.io'

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
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Profile', '/profile'),
    ('Archives', '/archives'),
    ('Categories', '/categories'),
    ('Tags', '/tags'),
)
MEDIUS_CATEGORIES = {
    'Android': {
        'description': 'Android',
        'logo': 'https://developer.android.com/images/brand/Android_Robot.png',
        'thumbnail': 'https://developer.android.com/images/brand/Android_Robot_200.png'
    }
}
MEDIUS_AUTHORS = {
    'shikajiro': {
        'description': """
            Android App Freelance.
        """,
        'cover': 'https://pbs.twimg.com/profile_banners/5497592/1549893196/1500x500',
        'image': 'https://pbs.twimg.com/profile_images/1111646061376921600/4HgO1Ojg_400x400.jpg',
        'links': (('github', 'https://github.com/shikajiro'),
                  ('twitter-square', 'https://twitter.com/shikajiro')),
    }
}
# Social widget
SOCIAL = (('github', 'https://github.com/shikajiro'),
          ('twitter', 'https://twitter.com/shikajiro'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "pelican-themes/medius"
PLUGINS = []

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

GOOGLE_ANALYTICS = "UA-389036-10"
