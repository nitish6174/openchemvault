FROM ubuntu:16.04
MAINTAINER Nitish Garg "nitish.garg.6174@gmail.com"
RUN apt-get update -y
RUN apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    mongodb
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install numpy
WORKDIR /app/cclib
RUN python3 setup.py build
RUN python3 setup.py install
WORKDIR /app
RUN pip3 install -r requirements.txt
WORKDIR /app/flaskapp
ENTRYPOINT ["python3"]
CMD ["app.py"]
