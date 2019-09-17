#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = (
    'Antoine',
)

SITENAME = 'Carquefou gymnastique masculine'
SITEURL = 'https://gym.carquefou.fr'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = ('%d %B %Y')

DEFAULT_LANG = 'fr'

DEFAULT_PAGINATION = False

THEME = "theme"

MENUITEMS = (
    ('Accueil', '/index.html', 'mobile'),
#    ('Le club', '/index.html#club', 'wide'),
    ('Actualités', '/blog.html', 'mobile'),
    ('Informations', '/infos.html', 'mobile'),
#    ('Galerie', '/index.html', 'mobile'),
    ('Contact', '/index.html#infospratiques', 'wide'),
)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DIRECT_TEMPLATES = ['index', 'blog']
STATIC_PATHS = ['images',
                'assets',
                #'extra/CNAME',
                'files',
                'static/robots.txt']
EXTRA_PATH_METADATA = {
#    'extra/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
}
PLUGIN_PATHS = ["plugins", ]
PLUGINS = ["include_assets", "sitemap", ]

SITEMAP = {
    'format': "xml"
}

#ARTICLE_EXCLUDES = ['documents', ]
#PAGE_EXCLUDES = ['documents', ]

RELATIVE_URLS = True

