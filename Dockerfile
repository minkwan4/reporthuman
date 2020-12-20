FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/minkwan4/reporthuman.git

WORKDIR /home/reporthuman/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=reporthuman.settings.deploy && gunicorn reporthuman.wsgi --env DJANGO_SETTINGS_MODULE=reporthuman.settings.deploy --bind 0.0.0.0:8000"]
