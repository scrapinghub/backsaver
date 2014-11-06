FROM ubuntu:12.04
RUN apt-get update
RUN apt-get install -y --force-yes python-dev 
RUN apt-get install -y python-pip
RUN apt-get install -y git
RUN pip install --upgrade pip
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ADD . /app
WORKDIR /app
CMD python backsaver.py 
EXPOSE 9418

