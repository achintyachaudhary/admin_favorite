import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='admin_favorite',
    version='1.0',
    packages=['admin_favorite'],
    package_data={
        "admin_favorite": ["migrations/*.py", "static/images/*.svg", "static/js/*.js", "templates/admin/*.html"],
    },
    description='Mark most used app to favorite in Django admin',
    long_description=README,
    author='Achintya Ranjan Chaudhary',
    author_email='achintyac77@gmail.com',
    url='https://github.com/achintyachaudhary/admin_favorite/',
    license='MIT',
    install_requires=[]
)
