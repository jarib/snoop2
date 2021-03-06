from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

DEBUG = True
SECRET_KEY = 'placeholder key for development'
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'snoop.data',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'snoop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'snoop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'snoop2',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = str(base_dir / 'static')

SNOOP_COLLECTIONS_ELASTICSEARCH_URL = 'http://localhost:9200'

SNOOP_BLOB_STORAGE = str(base_dir / 'blobs')
SNOOP_TIKA_URL = 'http://localhost:9998'
SNOOP_GNUPG_HOME = None
SNOOP_FEED_PAGE_SIZE = 100
SNOOP_STATS_ELASTICSEARCH_URL = None
SNOOP_STATS_ELASTICSEARCH_INDEX_PREFIX = 'snoop2-'
