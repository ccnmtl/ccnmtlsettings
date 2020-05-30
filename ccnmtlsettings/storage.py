from storages.backends.s3boto3 import S3Boto3Storage


class CompressorS3Boto3Storage(S3Boto3Storage):
    location = 'media'


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = 'uploads'
