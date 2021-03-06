import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'sqlalchemy',
    'pyramid_tm',
    'zope.sqlalchemy'
    ]

setup(name='edu_site',
      version='0.0',
      description='edu_site',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='mohammad ali nasrollahi',
      author_email='ma.nasrollahi71@yahoo.com',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="edu_site",
      entry_points="""\
      [paste.app_factory]
      main = edu_site:main
      initialize_edu_site_db = edu_site.initialize_db:main
      """,
      )
