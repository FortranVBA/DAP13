FROM python:3.7-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
CMD if [ "$DEBUG_DJANGO" = "True" ] ; then python manage.py runserver 0.0.0.0:8000 ; else gunicorn oc_lettings_site.wsgi ; fi
