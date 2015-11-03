from setuptools import setup

setup(name='riot_league_api',
    version='0.1',
    description='A Python wrapper to easily use Riots League of Legends API',
    url='http://github.com/peteryao',
    author='Peter Yao',
    author_email='peteryao916@gmail.com',
    license='MIT',
    packages=['riot_league_api'],
    install_requires=[
        'requests'
      # -*- Extra requirements: -*-
    ],
    zip_safe=False)