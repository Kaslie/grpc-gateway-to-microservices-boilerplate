FROM python:3.6
WORKDIR /home/app/

RUN apt-get -y update
RUN apt-get -y install python-dev build-essential
RUN apt-get -y install python-pip
RUN pip install --upgrade pip

ADD ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
ADD . .

ENV PORT 5001
EXPOSE 5001
CMD gunicorn -c gunicorn.py application:main
