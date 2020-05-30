from storages.backends.s3boto3 import S3Boto3Storage


class UploadsS3Boto3Storage(S3Boto3Storage):
    location = 'uploads'
