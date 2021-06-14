import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PAGE_SIZE = 5

STATIC_URL = '/static/'
STATIC_DIRECTORY = os.path.join(BASE_DIR, 'static')

TEMPLATE_DIRECTORY = os.path.join(BASE_DIR, 'templates')
BASE_TEMPLATE_NAME = 'index.html'

DATABASE_URL = "sqlite:///./db.sqlite3"

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = []  # for development
# ALLOWED_HOSTS = ['*']  # for docker-compose
# ALLOWED_HOSTS = ["your-production-domain"]  # for production
