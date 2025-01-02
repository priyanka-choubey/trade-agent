FROM python:latest

LABEL Maintainer="priyanka-choubey"

WORKDIR /

COPY . .
RUN pip install -r requirements.txt

CMD [ "python", "./main.py"]