FROM ubuntu:20.04
WORKDIR /flask-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./ ./
CMD [ "python3", "app.py"]
