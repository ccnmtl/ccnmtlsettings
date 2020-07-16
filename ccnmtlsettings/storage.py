from django.core.files.storage import get_storage_class
from storages.backends.s3boto3 import S3Boto3Storage


# From https://django-compressor.readthedocs.io/en/stable/remote-storages/
class CachedS3Boto3Storage(S3Boto3Storage):
    """
    S3 storage backend that saves the files locally, too.
    """
    def __init__(self, *args, **kwargs):
        super(CachedS3Boto3Storage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        self.local_storage._save(name, content)
        super(CachedS3Boto3Storage, self).save(name, self.local_storage._open(name))
        return name


class CompressorS3Boto3Storage(CachedS3Boto3Storage):
    location = 'media'


class MediaRootS3Boto3Storage(CachedS3Boto3Storage):
    location = 'uploads'
