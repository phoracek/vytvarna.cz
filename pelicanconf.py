# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = u'Výtvarna'
SITEURL = '/'
AUTHOR = u'Petr Horáček, TODO'

TIMEZONE = 'Europe/Prague'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%d. %m. %Y'

PLUGIN_PATH = 'plugins'
PLUGINS = ['lightbox']

PATH = 'content'

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'}}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

FILENAME_METADATA = '(?P<date>\d{4}\d{2}\d{2})_(?P<slug>[^_]*)'

ARTICLE_SAVE_AS = 'articles/{category}/{slug}-{lang}.html'
ARTICLE_URL = 'articles/{category}/{slug}-{lang}.html'

AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
