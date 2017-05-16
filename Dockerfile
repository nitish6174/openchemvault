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
    aptitude
# Start MongoDB server
RUN service mongodb start
# Copy source code
COPY . /app
# cd to source directory
WORKDIR /app
# Install pip dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# Install cclib
RUN aptitude install -y cclib
# Goto flaskapp directory to copy config file
WORKDIR /app/flaskapp
RUN cp config.py.example config.py
# Start flask application
ENTRYPOINT ["python3"]
CMD ["app.py"]
