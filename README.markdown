[![Actions Status](https://github.com/ccnmtl/ccnmtlsettings/workflows/build-and-test/badge.svg)](https://github.com/ccnmtl/ccnmtlsettings/actions)

These are the common settings we use across all our Django apps,
extracted into a handy reusable module.

## Usage

### Installation

First, install it with

    $ pip install ccnmtlsettings

or add `ccnmtlsettings==0.1.0` to your `requirements.txt`.

### Dependencies

The following libraries are used in some way, so they'll need to be installed:

* django_compressor
* django-debug-toolbar
* django-waffle
* coverage
* django-smoketest
* django-extensions
* django-statsd-mozilla
* django-markwhat
* django-storages
* django-impersonate
* boto3
* sentry-sdk
* statsd
* gunicorn
* django-cas-ng

### Use it

`ccnmtlsettings` has three "environments" (for now) that you will want
to make use of: `shared`, `staging`, and `production`.

In your `settings_shared.py` you will want to do something like:

	import os.path
	from ccnmtlsettings.shared import common

	project = 'yourapp'
	base = os.path.dirname(__file__)

	locals().update(common(project=project, base=base))

    # which apps should jenkins include in coverage reports?
	PROJECT_APPS = [
		'yourapp.main',
	]

	INSTALLED_APPS += [  # noqa
		'yourapp.main',
	]


Most of the magic is on the `locals().update(...)` line. That's where
the `common` function from `ccnmtlsettings.shared` is called with
simple configuration and returns a bunch of variables, which are then
injected into the local symbol table. The two requires parameters are
`project` and `base`.

`project` is the name of your project. It should be lowercase with
just alphanumeric characters. Most likely, just the name of the
directory for your project.

`base` is the full path of the directory that `settings_shared.py` is
in.

After that, a few settings that `ccnmtlsettings` can't fully set up are
set and/or modified. In particular, the project's apps are added to
`INSTALLED_APPS`.

An important note is that because of the weird symbol table tweaking
done earlier, flake8 will complain if you try to modify a variable
that comes out of `ccnmtlsettings`, since it didn't see where it got
defined. You need to add the `# noqa` line to each variable that you
modify this way to get it to ignore it.

You'll do almost the same thing for your `settings_staging.py` and
`settings_production.py`:

	from myapp.settings_shared import *
	from ccnmtlsettings.staging import common
	import os

	project = 'yourapp'
	base = os.path.dirname(__file__)

	locals().update(
		common(
			project=project,
			base=base,
			STATIC_ROOT=STATIC_ROOT,
			INSTALLED_APPS=INSTALLED_APPS,
			cloudfront='some-cloudfront-id',
		))

	try:
		from myapp.local_settings import *
	except ImportError:
		pass

(and the same thing for `settings_production.py`, but with `from
ccnmtlsettings.production import common` instead.)

Again, you are passing in `project`, and `base`. The
staging/production settings also need to have access to `STATIC_ROOT`
and `INSTALLED_APPS`, so those must be passed in.

Finally, there are a couple variables related to static file
deployment that you may or may not want to set:

`s3static` is a boolean. It defaults to `True` and tells
`ccnmtlsettings` that you are using S3 for serving static
files. Mainly, you will want to set this to `False` if your
application is not yet serving static files off S3.

`cloudfront` is a cloudfront id. If you pass it in, AWS Cloudfront
will be used for the static files URLs.

## Recommendations

If you're converting an existing app to `ccnmtlsettings`, which I
recommend is:

* install `ccnmtlsettings` and any libraries it requires
* add the `ccnmtlsettings` related stuff to the top of your
  `settings_shared.py` and set up the basic configuration, but leave
  all your settings in place after it (effectively overriding
  everything that `ccnmtlsettings` is pulling in).
* pull up
  https://github.com/ccnmtl/ccnmtlsettings/blob/master/ccnmtlsettings/shared.py
  in a browser.
* line by line, setting by setting, compare what you have in your
  `settings_shared.py` with what `ccnmtlsettings` has for the same
  variable. Delete yours if they are the same. Otherwise leave yours
  in place (or append the differences if it's a list variable).
* run your tests/flake8 each time.
* do the same for staging/production.
