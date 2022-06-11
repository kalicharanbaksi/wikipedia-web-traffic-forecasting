FROM ubuntu
WORKDIR /flask-docker
COPY requirements.txt requirements.txt
RUN apt-get -y install python3-pip
RUN pip3 install -r requirements.txt
COPY ./ ./
CMD [ "python3", "app.py"]
