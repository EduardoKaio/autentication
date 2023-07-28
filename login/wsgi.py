"""
WSGI config for login project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')

application = get_wsgi_application()
<<<<<<< HEAD
app = application
=======
app = application
>>>>>>> 9771c80cd18a84760d298cae968cf8756443c6de
