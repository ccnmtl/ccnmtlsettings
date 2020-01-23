import os.path
import sys


def common(**kwargs):
    # required args
    project = kwargs['project']
    base = kwargs['base']

    DEBUG = True

    ADMINS = []
    MANAGERS = ADMINS

    ALLOWED_HOSTS = [
        '.ctl.columbia.edu',
        '.ccnmtl.columbia.edu',
        'localhost',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': project,
            'HOST': '',
            'PORT': 5432,
            'USER': '',
            'PASSWORD': '',
            'ATOMIC_REQUESTS': True,
        }
    }

    if 'test' in sys.argv or 'jenkins' in sys.argv:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
                'HOST': '',
                'PORT': '',
                'USER': '',
                'PASSWORD': '',
                'ATOMIC_REQUESTS': True,
            }
        }

        PASSWORD_HASHERS = (
            'django.contrib.auth.hashers.MD5PasswordHasher',
        )

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

    TIME_ZONE = 'America/New_York'
    LANGUAGE_CODE = 'en-us'
    SITE_ID = 1
    USE_I18N = False
    MEDIA_ROOT = "/var/www/" + project + "/uploads/"
    MEDIA_URL = '/uploads/'
    STATIC_URL = '/media/'
    SECRET_KEY = 'you must override this'
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(base, "templates"),
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                    # list if you haven't customized them:
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.template.context_processors.request',
                    'django.contrib.messages.context_processors.messages',
                    'djangowind.context.context_processor',
                    'stagingcontext.staging_processor',
                    'gacontext.ga_processor',
                ],
            },
        },
    ]

    MIDDLEWARE = [
        'django_statsd.middleware.GraphiteRequestTimingMiddleware',
        'django_statsd.middleware.GraphiteMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'waffle.middleware.WaffleMiddleware',
        'impersonate.middleware.ImpersonateMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware'
    ]

    ROOT_URLCONF = project + '.urls'

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.flatpages',
        'django.contrib.staticfiles',
        'django.contrib.messages',
        'django.contrib.admin',
        'django_statsd',
        'smoketest',
        'gunicorn',
        'compressor',
        'djangowind',
        'impersonate',
        'waffle',
        'django_markwhat',
    ]

    INTERNAL_IPS = ['127.0.0.1']

    STATSD_CLIENT = 'statsd.client'
    STATSD_PREFIX = project
    STATSD_HOST = 'localhost'
    STATSD_PORT = 8125

    THUMBNAIL_SUBDIR = "thumbs"
    EMAIL_SUBJECT_PREFIX = "[" + project + "] "
    EMAIL_HOST = 'localhost'
    SERVER_EMAIL = project + "@mail.ctl.columbia.edu"
    DEFAULT_FROM_EMAIL = SERVER_EMAIL

    STATICMEDIA_MOUNTS = [
        ('/sitemedia', 'sitemedia'),
    ]

    # CAS settings

    AUTHENTICATION_BACKENDS = [
        'djangowind.auth.SAMLAuthBackend',
        'django.contrib.auth.backends.ModelBackend',
    ]

    CAS_BASE = "https://cas.columbia.edu/"
    WIND_PROFILE_HANDLERS = ['djangowind.auth.CDAPProfileHandler']
    WIND_AFFIL_HANDLERS = [
        'djangowind.auth.AffilGroupMapper',
        'djangowind.auth.StaffMapper',
        'djangowind.auth.SuperuserMapper',
    ]
    WIND_STAFF_MAPPER_GROUPS = ['tlc.cunix.local:columbia.edu']
    WIND_SUPERUSER_MAPPER_GROUPS = [
        'amm8',
        'mar227',
        'nb2413',
        'njn2118',
        'sld2131',
        'zm4',
    ]

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
    SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True

    STATIC_ROOT = "/tmp/" + project + "/static"
    STATICFILES_DIRS = ["media/"]
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ]

    COMPRESS_URL = "/media/"
    COMPRESS_ROOT = STATIC_ROOT

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
    }

    GRAPHITE_BASE = "https://graphite.ctl.columbia.edu/render/"

    return locals()
