from setuptools import setup, find_packages

setup(
    name="ccnmtlsettings",
    version="0.3.0",
    author="Anders Pearson",
    author_email="anders@columbia.edu",
    url="https://github.com/ccnmtl/ccnmtlsettings",
    description="CCNMTL common Django base settings",
    long_description="common settings we use across all our projects",
    install_requires = [
        "django_compressor",
        "django-debug-toolbar",
        "django-waffle",
        "django-jenkins",
        "django-smoketest",
        "django-extensions",
        "django-statsd-mozilla",
        "raven",
        "django-markwhat",
        "django-storages-redux",
        "django-cacheds3storage",
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
