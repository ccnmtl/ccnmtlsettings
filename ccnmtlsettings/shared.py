import os.path
import sys


def common(**kwargs):
    # required args
    project = kwargs['project']
    base = kwargs['base']

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

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

    JENKINS_TASKS = [
        'django_jenkins.tasks.run_pep8',
        'django_jenkins.tasks.run_pyflakes',
    ]

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

    TIME_ZONE = 'America/New_York'
    LANGUAGE_CODE = 'en-us'
    SITE_ID = 1
    USE_I18N = False
    MEDIA_ROOT = "/var/www/" + project + "/uploads/"
    MEDIA_URL = '/uploads/'
    STATIC_URL = '/media/'
    SECRET_KEY = 'you must override this'
    TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]

    TEMPLATE_CONTEXT_PROCESSORS = [
        'django.contrib.auth.context_processors.auth',
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.messages.context_processors.messages',
        'django.template.context_processors.static',
        'djangowind.context.context_processor',
        'stagingcontext.staging_processor',
        'gacontext.ga_processor',
    ]

    MIDDLEWARE_CLASSES = [
        'django_statsd.middleware.GraphiteRequestTimingMiddleware',
        'django_statsd.middleware.GraphiteMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'waffle.middleware.WaffleMiddleware',
        'impersonate.middleware.ImpersonateMiddleware',
    ]

    ROOT_URLCONF = project + '.urls'

    TEMPLATE_DIRS = [
        os.path.join(base, "templates"),
    ]

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
        'debug_toolbar',
        'django_jenkins',
        'gunicorn',
        'compressor',
        'djangowind',
        'impersonate',
        'waffle',
        'django_markwhat',
    ]

    INTERNAL_IPS = ['127.0.0.1']
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
    ]

    STATSD_CLIENT = 'statsd.client'
    STATSD_PREFIX = project
    STATSD_HOST = 'localhost'
    STATSD_PORT = 8125

    THUMBNAIL_SUBDIR = "thumbs"
    EMAIL_SUBJECT_PREFIX = "[" + project + "] "
    EMAIL_HOST = 'localhost'
    SERVER_EMAIL = project + "@ccnmtl.columbia.edu"
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
        'anp8',
        'jb2410',
        'mar227',
        'njn2118',
        'sld2131',
        'zm4',
    ]

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
    SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
    SESSION_COOKIE_HTTPONLY = True

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

    GRAPHITE_BASE = "https://nanny-render.cul.columbia.edu/render/"

    return locals()
