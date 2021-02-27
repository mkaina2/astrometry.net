from __future__ import absolute_import
# settings_nova.py
import os, sys
from astrometry.net.settings_common import *
from astrometry.net.settings_social2 import *

sitename = 'nova'
ALLOWED_HOSTS = ["astrometry.kaina.fr","localhost"]
MULTI_HOSTS = []

# from settings_social import *
# ENABLE_SOCIAL = True
# SOUTH_MIGRATION_MODULES.update(SOCIAL_MIGRATION)
# TEMPLATE_CONTEXT_PROCESSORS += SOCIAL_TEMPLATE_CONTEXT_PROCESSORS
# INSTALLED_APPS += SOCIAL_INSTALLED_APPS 
# AUTHENTICATION_BACKENDS = SOCIAL_AUTH_BACKENDS + AUTHENTICATION_BACKENDS

WCS2KML = '/usr/local/wcs2kml/bin/wcs2kml'

ENABLE_SOCIAL = False
ENABLE_SOCIAL2 = True

os.environ['MPLCONFIGDIR'] = '/home/nova/.config/matplotlib'

INSTALLED_APPS += SOCIAL_INSTALLED_APPS 
AUTHENTICATION_BACKENDS = SOCIAL_AUTH_BACKENDS + AUTHENTICATION_BACKENDS
TEMPLATES[0]['OPTIONS']['context_processors'].extend(SOCIAL_TEMPLATE_CONTEXT_PROCESSORS)

USE_X_FORWARDED_HOST = True

TEMPDIR = '/tmp/astrometry'
DATABASES['default']['NAME'] = 'astrometry'
DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = 'django.sqlite3'


LOGGING['loggers']['django.request']['level'] = 'WARN'

import logging
logger = logging.getLogger('django.db.backends')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

SESSION_COOKIE_NAME = 'NovaAstrometrySession'

ssh_solver_config = 'an-nova'

try:
    SOCIAL_AUTH_GITHUB_KEY    = github_secrets[sitename].key
    SOCIAL_AUTH_GITHUB_SECRET = github_secrets[sitename].secret
except:
    SOCIAL_AUTH_GITHUB_KEY    = None
    SOCIAL_AUTH_GITHUB_SECRET = None
    
