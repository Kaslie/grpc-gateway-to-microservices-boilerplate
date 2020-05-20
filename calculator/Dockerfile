FROM python:3.6 as builder
WORKDIR /home/app/

RUN apt-get -y update
RUN apt-get -y install python-dev build-essential
RUN apt-get -y install python-pip
RUN pip install --upgrade pip

ADD ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
ADD . .

FROM builder
COPY --from=amothic/grpc-health-probe . .

ENV PORT 5001
EXPOSE 5001
