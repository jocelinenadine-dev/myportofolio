# ==============================================================================
# [TUTORIAL 1 & DEPLOYMENT PWS]: WSGI (Web Server Gateway Interface)
# File ini digunakan oleh web server produksi (seperti Gunicorn di PWS) untuk 
# menghubungkan server web ke aplikasi Django Anda.
# ==============================================================================

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio.settings')

application = get_wsgi_application()
