FROM python:3.7-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
CMD gunicorn oc_lettings_site.wsgi -b 0.0.0.0:8000
