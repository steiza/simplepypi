from python:latest

ADD . .
RUN python setup.py install

CMD simplepypi/bin/simplepypi --addr 0.0.0.0
