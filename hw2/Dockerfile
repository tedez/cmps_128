FROM ubuntu:16.04
# RUN apt-get update -y
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python hw2.py