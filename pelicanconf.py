#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'rbrianaaron'
SITENAME = u'rbrianaaron'
SITEURL = 'http://rbrianaaron.github.io/blog/'

PATH = 'content'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/rbrianaaron'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "C:/Users/Brian/virtualenvs/pelican/pelican-themes/bootstrap2"

STATIC_PATHS = ['images']

DISPLAY_PAGES_ON_MENU = True

LOAD_CONTENT_CACHE = False

DEFAULT_DATE = 'fs'


#DIRECT_TEMPLATES  = (('tags'),)
TAGS_SAVE_AS = 'tags.html'
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100