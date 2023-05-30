"""
WSGI config for Ukraine project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ukraine.settings')


application = get_wsgi_application()
app = application

# import os
# import time
# import traceback
# import signal
# import sys
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ukraine.settings')

# try:
#     application = get_wsgi_application()
#     print('WSGI without exception')
# except Exception as e:
#     print('handling WSGI exception',e)
#     # Error loading applications
#     if 'mod_wsgi' in sys.modules:
#         traceback.print_exc()
#         os.kill(os.getpid(), signal.SIGINT)
#         time.sleep(2.5)