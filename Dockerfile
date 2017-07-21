FROM ubuntu:16.04
MAINTAINER Nitish Garg "nitish.garg.6174@gmail.com"
# Install apt dependencies
RUN apt-get update -y && apt-get install -y \
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
# Upgrade pip
RUN pip3 install --upgrade pip
# Start MongoDB server
RUN service mongodb start
# Install cclib
RUN mkdir /cclib && \
    wget https://github.com/cclib/cclib/releases/download/v1.5/cclib-1.5.post1.tar.gz && \
    tar -xf cclib-1.5.post1.tar.gz -C /cclib/ && \
    pip3 install numpy
WORKDIR /cclib/cclib-1.5.post1
RUN python3 setup.py build && \
    python3 setup.py install
# Install OpenBabel
RUN mkdir /openbabel && \
    wget https://github.com/openbabel/openbabel/archive/openbabel-2-4-1.tar.gz && \
    tar -xf openbabel-2-4-1.tar.gz -C /openbabel/ && \
    mkdir /openbabel/build
RUN mkdir /app
WORKDIR /openbabel/build
RUN cmake /openbabel/openbabel-openbabel-2-4-1 -DPYTHON_BINDINGS=ON && \
    make && \
    make install
# Install pip dependencies
COPY ./requirements.txt /pip/
RUN pip3 install -r /pip/requirements.txt
# Copy source directory
COPY . /app
# Goto flaskapp directory to copy config file
WORKDIR /app/flaskapp
RUN cp config.py.example config.py
WORKDIR /app
