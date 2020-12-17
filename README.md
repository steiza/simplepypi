#### This is a really, really, simple HTTP PyPI-like server.

It is intended to be used for companies or organizations that need a private
PyPi.

It literally supports four functions:

    - Allows uploading of packages
    - Downloading by package (or package and version)
    - A / page that is navigatable with a web browser
    - /pypi/ listing

It does not support:

    - Stopping you from overwriting a package with the same name / version
    - Registering packages
    - Any sort of ACLs

To use it run "simplepypi". You can upload packages by:

#### Install twine if you haven't already:

    pip install twine

#### Build your package if you haven't already:

    python setup.py sdist

#### Upload your package using twine:

    $ twine upload --repository-url http://127.0.0.1:8000/ dist/*
    Uploading distributions to http://127.0.0.1:8000/
    Enter your username: <whatever>
    Enter your password: <doesn't matter, see above>

#### Then, when you want to install packages from it you do:

    pip install -i http://127.0.0.1:8000/pypi <your favorite package>
    
#### Or, if you're stuck in the stone ages with `setuptools`/`easy_install`:

    from setuptools import setup

    setup(
        ...
        install_requires=['<package>'],
        dependency_links=['http://127.0.0.1:8000/packages/<package>'],
    )
    
    python setup.py install

#### To use the docker image, build and run:

    docker build -t simplepypi .
    docker run -it -p 8000:8000 simplepypi

Not using twine yet? Here is the legacy way of uploading Python packages (not
recommended):

#### Modify your ~/.pypirc so it looks like:

    [distutils]
    index-servers =
        pypi
        local

    [local]
    username: <whatever>
    password: <doesn't matter, see above>
    repository: http://127.0.0.1:8000

    [pypi]
    ...

#### Run this on the setup.py of your favorite package:

    $ python setup.py sdist upload -r local

And that's it!
