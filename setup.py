from codecs import open as codecs_open
from setuptools import setup, find_packages

setup(name='vendfinder',
      version='0.0.1',
      classifiers=[],
      keywords='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'flask-bootstrap',
          'gunicorn'
      ],
      extras_require={
          'test': ['pytest'],
      },
      #entry_points="""
      #[console_scripts]
      #vendfinder=vendfinder.views.vendfinderview:cli
      #"""
      )
