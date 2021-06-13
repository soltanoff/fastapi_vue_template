PAGE_SIZE = 5

STATIC_URL = '/static/'
STATIC_DIRECTORY = 'static'

TEMPLATE_DIRECTORY = 'templates'
BASE_TEMPLATE_NAME = 'index.html'

DATABASE_URL = "sqlite:///./db.sqlite3"

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = []  # for development
# ALLOWED_HOSTS = ['*']  # for docker-compose
# ALLOWED_HOSTS = ["your-production-domain"]  # for production
