FROM ubuntu:16.04
MAINTAINER Nitish Garg "nitish.garg.6174@gmail.com"
# Install apt dependencies
RUN apt-get update -y
RUN apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    mongodb \
    wget \
    tar \
    make \
    cmake \
    swig
# Start MongoDB server
RUN service mongodb start
# Upgrade pip
RUN pip3 install --upgrade pip
# Install cclib
RUN mkdir /cclib
RUN wget https://github.com/cclib/cclib/releases/download/v1.5/cclib-1.5.post1.tar.gz
RUN tar -xf cclib-1.5.post1.tar.gz -C /cclib/
RUN pip3 install numpy
WORKDIR /cclib/cclib-1.5.post1
RUN python3 setup.py build
RUN python3 setup.py install
# Install OpenBabel
RUN mkdir /openbabel
RUN wget https://github.com/openbabel/openbabel/archive/openbabel-2-4-1.tar.gz
RUN tar -xf openbabel-2-4-1.tar.gz -C /openbabel/
RUN mkdir /openbabel/build
WORKDIR /openbabel/build
RUN cmake /openbabel/openbabel-openbabel-2-4-1 -DPYTHON_BINDINGS=ON -DRUN_SWIG=ON
RUN make
RUN make install
# Install pip dependencies
COPY ./requirements.txt /pip/
RUN pip3 install -r /pip/requirements.txt
# Goto source directory
COPY . /app
WORKDIR /app
# Goto flaskapp directory to copy config file
WORKDIR /app/flaskapp
RUN cp config.py.example config.py
# Start flask application
ENTRYPOINT ["python3"]
CMD ["app.py"]
