FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip 

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r ./src/requirements/base.txt

CMD [ "python",  "./src/app.py" ]
