# YOLOv5 🚀 by Ultralytics, GPL-3.0 license

# docker image build
# docker build --tag canary_yolo:{version} .

# docker run image
# sudo docker run -it canary_yolo:1.1 /bin/bash

# We don't need large linux image! Running on azureml
FROM debian:buster

# TEAM Canary OSAM
LABEL email="zheedong@gmial.com"
LABEL name="Canary"
LABEL version="1.0"
LABEL description="OSAM Hackerthon"

# Install linux packages
RUN apt update && apt install -y zip htop screen libgl1-mesa-glx

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

# Install sudo
RUN apt-get update \
 && apt-get install -y sudo

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# USER docker

# libffi package 연결
# RUN sudo ln -s /usr/lib/x86_64-linux-gnu/libffi.so.7 /usr/lib/x86_64-linux-gnu/libffi.so.6

# Install python dependencies
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache -r requirements.txt 

# TODO : Add python to PATH
# RUN export PATH=/Users/docker/Library/Python/3.7/bin:$PATH

# requirements for detection
# RUN python3 -m pip install --no-cache -qr https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt
# RUN python3 -m pip install opencv-python googledrivedownloader

# Create working directory
RUN sudo mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy contents
COPY . /usr/src/app

# Set environment variables
ENV HOME=/usr/src/app

# Usage Examples -------------------------------------------------------------------------------------------------------

# Train
ENTRYPOINT ["sudo", "python3", "train_with_azure.py"]

# Detect
# ENTRYPOINT ["sudo", "python3", "detect.py"]