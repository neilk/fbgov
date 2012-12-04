#!/usr/bin/env python

import bleach
import logging
import sys

logging.basicConfig()

text = file(sys.argv[1]).read()

allowedTags = list(bleach.ALLOWED_TAGS)
allowedTags.extend(['div', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'html', 'body', 'head', 'title'])

print bleach.clean(text, tags=allowedTags, strip=True).encode('utf8');


