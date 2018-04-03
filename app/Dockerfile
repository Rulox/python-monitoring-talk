#FROM python:3
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
ADD . /app 
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
