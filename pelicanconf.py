#!/usr/bin/env python
# -*- coding: utf-8 -*- #
""" Pelican configuration file """

from __future__ import unicode_literals

AUTHORS = (
    'Antoine',
)

SITENAME = 'Carquefou gymnastique masculine'
SITEURL = 'https://gym.carquefou.fr'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
DEFAULT_DATE_FORMAT = ('%d %B %Y')

# DEFAULT_PAGINATION = False

THEME = "theme"

MENUITEMS = (
    ('Accueil', '/index.html', 'mobile'),
    ('Actualités', '/blog.html', 'mobile'),
    ('Informations', '/infos.html', 'mobile'),
    ('Contact', '/index.html#infospratiques', 'wide'),
)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DIRECT_TEMPLATES = ['index', 'blog']

STATIC_PATHS = ['images',
                'assets',
                'files',
                'static/robots.txt']

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
}

PLUGIN_PATHS = ["plugins", ]
PLUGINS = ["include_assets", "sitemap", ]

SITEMAP = {
    'format': "xml"
}

# Prevents the creation of /category/ and /authors/
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''

# ARTICLE_EXCLUDES = ['documents', ]
# PAGE_EXCLUDES = ['documents', ]

# RELATIVE_URLS = True
