# ==============================================================================
# [TUTORIAL 1]: ASGI (Asynchronous Server Gateway Interface)
# File konfigurasi standar Django untuk mendukung protokol asinkronus (async).
# ==============================================================================

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio.settings')

application = get_asgi_application()
