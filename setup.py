from setuptools import setup, find_packages

setup(
    name="ccnmtlsettings",
    version="1.8.4",
    author="Anders Pearson",
    author_email="ctl-dev@columbia.edu",
    url="https://github.com/ccnmtl/ccnmtlsettings",
    description="CCNMTL common Django base settings",
    long_description="common settings we use across all our projects",
    install_requires = [
        "django_compressor",
        "django-debug-toolbar",
        "django-waffle",
        "coverage",
        "django-smoketest",
        "django-extensions",
        "django-statsd-mozilla",
        "sentry-sdk",
        "django-markwhat",
        "django-storages-redux",
        "boto3",
        "statsd",
        "gunicorn",
        "djangowind",
        "django-impersonate",
    ],
    scripts = [],
    license = "BSD",
    platforms = ["any"],
    zip_safe=False,
    package_data = {'' : ['*.*']},
    packages=['ccnmtlsettings'],
    )
