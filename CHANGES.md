1.4.0
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
