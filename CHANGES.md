1.9.1 (2021-08-04)
==================
* Fix postgresql engine name
* Removed AWS S3 'public-read' default setting

1.9.0 (2020-09-15)
==================
* Remove python 2 support
* django-storages settings update

1.8.4 (2020-07-16)
==================
* Use django-cacheds3storage again, for
  django-compressor/django-storages integration.

1.8.3 (2020-06-01)
==================
* Specify directories for static & uploaded files

1.8.2 (2020-05-28)
==================
* Fix s3boto3 module path name

1.8.1 (2020-05-28)
==================
* Use s3boto3 storage backend from django-storages, for compatibility
  with django-storages>=1.9.0.

1.8.0 (2020-01-23)
==================
* Replace django-jenkins with coverage

1.7.0 (2019-11-22)
==================
* Add XFrameOptionsMiddleware
* Add SecurityMiddleware
* Flag CSRF and Session cookie as secure
* Flag CSRF and Session cookie as http only


1.6.0 (2019-11-08)
==================
* Add AWS_DEFAULT_ACL = 'public-read'
* Use boto3 in docker settings
* Remove raven, replace with sentry-sdk

1.5.0 (2019-01-31)
==================
* Update SERVER_EMAIL to project@mail.ctl.columbia.edu

1.4.0 (2018-03-13)
==================

* Support both `MIDDLEWARE` and `MIDDLEWARE_CLASSES`.

1.3.1 (2017-06-30)
==================

* deactivating anders

1.3.0 (2017-01-20)
==================

* point at our local graphite base

1.2.0 (2016-10-26)
==================

* remove `jb2410` from superusers list
* add Nick B to superusers list

1.1.2 (2016-09-26)
==================

* fixed syntax error in `compose.py`

1.1.1 (2016-09-23)
==================

* flake8

1.1.0 (2016-09-23)
==================

* allow S3 bucket prefix to be overridden with the `s3prefix`
  parameter
* add docker and docker-compose settings

1.0.0 (2016-08-03)
==================

* NOT BACKWARDS COMPATIBLE: converted `TEMPLATES` setting to new style
  (Django 1.10 compatible). If you are modifying any template settings
  in `settings_staging.py`, `settings_production.py`, etc. you will
  now need to copy in and override the entire `TEMPLATES` block
  instead.

0.3.0 (2016-07-07)
==================

* add `.ctl.columbia.edu` to `ALLOWED_HOSTS`

0.2.0 (2016-04-01)
==================

* remove cld2156 from admin list

0.1.6 (2016-03-12)
==================
* select a significantly faster password hashing method for unit tests

0.1.5 (2016-02-24)
==================
* include Cassandra in superusers list

0.1.4 (2016-01-28)
==================
* set DEFAULT_FROM_EMAIL

0.1.3 (2015-12-17)
==================
* fix MEDIA_ROOT path for staging

0.1.2 (2015-12-16)
==================
* fix MEDIA_URL path bug with s3 static files

0.1.1 (2015-12-14)
==================

* fix path bug with s3 static files (non-cloudfront)
