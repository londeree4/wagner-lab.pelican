#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site details
AUTHOR = u'wagnerlab'
SITENAME = u'Wagner Lab'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'EST'
DEFAULT_LANG = u'en'
PAGE_ORDER_BY = 'page-order'

# Fix to put pages in root and blog under a blog directory
# effectively inverting how pelican normally works
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
# we need to change the main index page now though...
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'
#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
CATEGORIES_URL = 'blog/category/'
CATEGORIES_SAVE_AS = 'blog/category/index.html'
TAG_URL = 'blog/tag/{slug}.html'    
TAG_SAVE_AS = 'blog/tag/{slug}.html'    
TAGS_URL = 'blog/tag/'  
TAGS_SAVE_AS = 'blog/tag/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
ARCHIVES_URL = 'blog/archives/archives.html'
AUTHOR_SAVE_AS = 'blog/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
# put pages in the root directory
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# Theme
#THEME = '..\pelican-themes\pelican-bootstrap3'
#STATIC_PATHS = ['images']
#HEADER_IMAGE = 'header.png'

# Static paths
STATIC_PATHS = ['images','cv','extra/robots.txt','extra/favicon.ico','extra/CNAME']

# Use this trick to add favicon and robots to output
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
					   'extra/favicon.ico': {'path': 'favicon.ico'},
					   'extra/CNAME': {'path': 'CNAME'},}

					   
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

		  
FACEBOOK_URL = None
TWITTER_URL = None
GITHUB_URL = 'https://github.com/wagner-lab'
COPY_TEXT = '©2015 Wagner Lab'
PELICAN_TEXT = 'The Wagner Lab is powered by <a href="http://getpelican.com/">Pelican</a>, <a href="http://python.org/">Python</a> & Nespresso'
		  
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Not used by bootbrain theme
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)
# Social widget
SOCIAL = (('Github', 'http://github.com/wagner-lab'),
          ('Another social link', '#'),)

ABOUT_ME = "Test"		  
		  

