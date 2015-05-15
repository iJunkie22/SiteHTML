__author__ = 'ethan'

from distutils.core import setup


setup(name='SiteHTML',
      version='1.0',
      author='Ethan Randall',
      author_email='iJunkie22@gmail.com',
      url='https://github.com/iJunkie22/SiteHTML',
      packages=['SiteHTML'],
      package_dir={'SiteHTML': 'SiteHTML'},
      package_data={'SiteHTML': ['images/*.png']},
      )