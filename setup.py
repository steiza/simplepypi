from setuptools import setup

setup(name='simplepypi',
        version='0.0.2',
        author='Zach Steindler',
        author_email='steiza@coffeehousecoders.org',
        url='http://github.com/steiza/simplepypi',
        description='A really, really, simple HTTP PyPI-like server',
        long_description='''It is intended to be used for companies or organizations that need a private PyPi''',
        keywords='pypi, replacement, cheeseshop',
        classifiers=['Programming Language :: Python', 'License :: OSI Approved :: BSD License'],
        license='BSD',
        packages=['simplepypi'],
        scripts=['simplepypi/bin/simplepypi'],
        install_requires=['twisted', 'txroutes'],
        )
