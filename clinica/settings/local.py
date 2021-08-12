import os
from .base import *
import dj_database_url 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Update database configuration with $DATABASE_URL.
 
db_from_env = dj_database_url.config(conn_max_age=500)  
DATABASES['default'].update(db_from_env)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (  
    os.path.join(BASE_DIR, 'static'),
)