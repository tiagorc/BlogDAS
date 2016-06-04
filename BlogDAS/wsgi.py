"""
WSGI config for BlogDAS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

path = '/home/blogdas/BlogDAS'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlogDAS.settings")

application = DjangoWhiteNoise(get_wsgi_application())
