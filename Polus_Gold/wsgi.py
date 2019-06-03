"""
WSGI config for Polus_Gold project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django inport DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Polus_Gold.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
