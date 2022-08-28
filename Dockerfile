FROM python:3.8

WORKDIR /nothingatallbitch
COPY requirements.txt /nothingatallbitch/
RUN pip3 install -r requirements.txt
COPY . /nothingatallbitch/

CMD python3 main.py
