import os.path
import sys


def common(**kwargs):
    # required args
    project = kwargs['project']
    base = kwargs['base']
    STATIC_ROOT = kwargs['STATIC_ROOT']
    INSTALLED_APPS = kwargs['INSTALLED_APPS']

    # optional args
    s3static = kwargs.get('s3static', True)
    cloudfront = kwargs.get('cloudfront', None)

    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    STAGING_ENV = True

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

    STATSD_PREFIX = project + "-staging"

    MEDIA_ROOT = '/var/www/' + project + '/mediamachine/uploads/'

    # put any static media here to override app served static media
    STATICMEDIA_MOUNTS = [
        ('/sitemedia', '/var/www/' + project + '/' + project + '/sitemedia'),
    ]

    if s3static:
        # serve static files off S3
        AWS_STORAGE_BUCKET_NAME = "ccnmtl-" + project + "-static-stage"
        AWS_PRELOAD_METADATA = True
        STATICFILES_STORAGE = 'cacheds3storage.CompressorS3BotoStorage'
        if cloudfront:
            AWS_S3_CUSTOM_DOMAIN = cloudfront + '.cloudfront.net'
            S3_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
            STATIC_URL = 'https://%s/media/' % AWS_S3_CUSTOM_DOMAIN
        else:
            S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
            STATIC_URL = ('https://%s.s3.amazonaws.com/compressor/'
                          % AWS_STORAGE_BUCKET_NAME)
        COMPRESS_ENABLED = True
        COMPRESS_OFFLINE = True
        COMPRESS_ROOT = STATIC_ROOT
        COMPRESS_URL = STATIC_URL
        DEFAULT_FILE_STORAGE = 'cacheds3storage.MediaRootS3BotoStorage'
        COMPRESS_STORAGE = 'cacheds3storage.CompressorS3BotoStorage'
        MEDIA_URL = S3_URL + '/media/'
        AWS_QUERYSTRING_AUTH = False
    else:
        # non S3 mode
        STATICFILES_DIRS = ()
        STATIC_ROOT = "/var/www/" + project + "/" + project + "/media/"
        COMPRESS_ROOT = STATIC_ROOT

    if 'migrate' not in sys.argv:
        INSTALLED_APPS.append('raven.contrib.django.raven_compat')

    return locals()