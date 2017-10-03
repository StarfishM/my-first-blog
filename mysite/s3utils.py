from storages.backends.s3boto import S3BotoStorage

# StaticS3BotoStorage = lambda: S3BotoStorage(location='static') might move static to S3 later
MediaS3BotoStorage = lambda: S3BotoStorage(location='media')
