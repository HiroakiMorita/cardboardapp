FROM python:3.7.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /api
WORKDIR /api
ADD ./requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8000
