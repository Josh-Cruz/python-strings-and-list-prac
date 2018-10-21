"""
WSGI config for survey project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

# import os
# import sys
# from django.core.wsgi import get_wsgi_application

# path = 'C:\Users\Josh\Desktop\Dojo_Assignments\Python\myEnvironments\djangoEnv\survey'
# if path not in sys.path:
#     sys.path.append(path)

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "survey.settings")

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'YOURAPP.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YOURAPP.settings")

application = get_wsgi_application()
