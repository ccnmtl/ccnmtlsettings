import os.path
import sys


def common(**kwargs):
    # required args
    project = kwargs['project']
    base = kwargs['base']
    STATIC_ROOT = kwargs['STATIC_ROOT']
    INSTALLED_APPS = kwargs['INSTALLED_APPS']

    DEBUG = False
    TEMPLATE_DEBUG = DEBUG

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': project,
            'HOST': '',
            'PORT': 6432,
            'USER': '',
            'PASSWORD': '',
            'ATOMIC_REQUESTS': True,
        }
    }

    TEMPLATE_DIRS = [
        os.path.join(base, "templates"),
    ]

    MEDIA_ROOT = '/var/www/' + project + '/mediamachine/uploads/'

    # put any static media here to override app served static media
    STATICMEDIA_MOUNTS = [
        ('/sitemedia', '/var/www/' + project + '/' + project + '/sitemedia'),
    ]

    AWS_STORAGE_BUCKET_NAME = "ccnmtl-" + project + "-static-stage"
    AWS_PRELOAD_METADATA = True
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = project + '.s3utils.CompressorS3BotoStorage'
    S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = ('https://%s.s3.amazonaws.com/compressor/'
                  % AWS_STORAGE_BUCKET_NAME)
    COMPRESS_ENABLED = True
    COMPRESS_OFFLINE = True
    COMPRESS_ROOT = STATIC_ROOT
    COMPRESS_URL = STATIC_URL
    DEFAULT_FILE_STORAGE = project + '.s3utils.MediaRootS3BotoStorage'
    MEDIA_URL = S3_URL + '/media/'
    COMPRESS_STORAGE = project + '.s3utils.CompressorS3BotoStorage'
    AWS_QUERYSTRING_AUTH = False

    if 'migrate' not in sys.argv:
        INSTALLED_APPS.append('raven.contrib.django.raven_compat')

    return locals()
