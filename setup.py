__author__ = 'ethan'

from distutils.core import setup


setup(name='SiteHTML',
      version='1.5.2',
      author='Ethan Randall',
      author_email='iJunkie22@gmail.com',
      url='https://github.com/iJunkie22/SiteHTML',
      packages=['SiteHTML'],
      package_dir={'SiteHTML': 'SiteHTML'},
      package_data={'SiteHTML': ['images/*.png']},
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Internet :: WWW/HTTP :: Site Management',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Text Editors :: Integrated Development Environments (IDE)',
                   'Topic :: Text Processing :: Markup',
                   'Topic :: Text Processing :: Markup :: HTML',
                   'Topic :: Utilities'],
      description='Python module to extract globals from a site index, then inject into the other .html files.',
      long_description='''Python module to extract globals from a site index, then inject into the other .html files.

        Check out the `wiki page <https://github.com/iJunkie22/SiteHTML/wiki/Sample-template>`_ on GitHub for usage.

        Check out the `README <https://github.com/iJunkie22/SiteHTML/blob/master/README.md>`_ on GitHub for how to use\
         with IDEs such as WebStorm.

        If using as a plugin in an IDE, you can find thumbnails in the images folder of the package, \
        where for example SiteHTML/imgages/SiteHTML_25.png is a 25x25 px icon.''',
      keywords=['html', 'refactor', 'index', 'global', 'globals']

      )