FROM Ubuntu

RUN apt update
RUN apt install python

COPY . /opt/source-code

RUN pip install -r requirements.txt
