from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='*bkpy@gy8cg$&#gmvv$=y*p%)nw%)vf8#$pt*$&93f&(_-c)h#')

DEBUG = env.bool('DJANGO_DEBUG', True)
