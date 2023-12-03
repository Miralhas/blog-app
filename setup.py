from setuptools import setup

setup(
    name="django-blog",
    version="0.1.0",
    packages=["djblog", "blog", "accounts"],
    install_requires=[
        "django",
        "django-crispy-forms",
        "crispy-bootstrap4",
        "django-markdownify",
        "django-widget-tweaks"
        "django-extensions"
    ],
)