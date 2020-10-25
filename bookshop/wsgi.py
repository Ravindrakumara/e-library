
import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise # for static file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookshop.settings')

application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(bookshop) # static load thought


""""
from whitenoise.django import DjangoWhiteNoise


"""
