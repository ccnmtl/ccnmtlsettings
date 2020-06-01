def common(**kwargs):
    # required args
    project = kwargs['project']
    base = kwargs['base']
    STATIC_ROOT = kwargs['STATIC_ROOT']
    INSTALLED_APPS = kwargs['INSTALLED_APPS']

    # optional args
    s3static = kwargs.get('s3static', True)
    cloudfront = kwargs.get('cloudfront', None)
    s3prefix = kwargs.get('s3prefix', 'ccnmtl')

    DEBUG = False

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

    MEDIA_ROOT = '/var/www/' + project + '/uploads/'

    STATICMEDIA_MOUNTS = [
        ('/sitemedia', '/var/www/' + project + '/' + project + '/sitemedia'),
    ]

    if s3static:
        # serve static files off S3
        AWS_STORAGE_BUCKET_NAME = s3prefix + "-" + project + "-static-prod"
        AWS_DEFAULT_ACL = 'public-read'
        AWS_PRELOAD_METADATA = True
        STATICFILES_STORAGE = 'ccnmtlsettings.storage.CompressorS3Boto3Storage'
        if cloudfront:
            AWS_S3_CUSTOM_DOMAIN = cloudfront + '.cloudfront.net'
            S3_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
            STATIC_URL = 'https://%s/media/' % AWS_S3_CUSTOM_DOMAIN
        else:
            S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
            STATIC_URL = ('https://%s.s3.amazonaws.com/media/'
                          % AWS_STORAGE_BUCKET_NAME)
        COMPRESS_ENABLED = True
        COMPRESS_OFFLINE = True
        COMPRESS_ROOT = STATIC_ROOT
        COMPRESS_URL = STATIC_URL
        DEFAULT_FILE_STORAGE = 'ccnmtlsettings.storage.MediaRootS3Boto3Storage'
        COMPRESS_STORAGE = 'ccnmtlsettings.storage.CompressorS3Boto3Storage'
        MEDIA_URL = S3_URL + 'uploads/'
        AWS_QUERYSTRING_AUTH = False
    else:
        # non S3 mode
        STATICFILES_DIRS = ()
        STATIC_ROOT = "/var/www/" + project + "/" + project + "/media/"
        COMPRESS_ROOT = STATIC_ROOT

    return locals()
