#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Amjith Ramanujam'
SITENAME = u'mycli'
SITEURL = 'http://mycli.net'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = 'feeds/tag.%s.rss.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('pgcli', 'http://pgcli.com/'),
         ('packagecloud', 'http://packagecloud.io/'),
        )

# Sponsors
SPONSORS = (('jweiland', 'https://jweiland.net/', 'theme/images/jweiland.png', 'left'),
            ('Tech Blue Software', 'http://www.techbluesoftware.co.in/', 'theme/images/techblue.png', 'right'),
            )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/amjithr'),
          ('github', 'http://github.com/dbcli/mycli'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

DIRECT_TEMPLATES = {}

STATIC_PATHS = {'images', 'extra/CNAME'}
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME = 'theme/notmyidea'
#THEME = 'blueidea'

GOOGLE_ANALYTICS = 'UA-64493707-1'
