FROM python:3.9.0

WORKDIR /home/

RUN echo "update.20.12/25:lottoapp"
RUN echo "update.20.12/30:points"


RUN git clone https://github.com/minkwan4/reporthuman.git

RUN echo "update.21.1/15:points"
RUN echo "update.21.1/15:fix1"
RUN echo "update.21.1/15:fix2"
RUN echo "update.21.1/15:fix3"
RUN echo "update.21.1/15:fix4"
RUN echo "update.21.1/15:fix5"
RUN echo "update.21.1/15:fix6"

WORKDIR /home/reporthuman/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=reporthuman.settings.deploy && python manage.py migrate --settings=reporthuman.settings.deploy && gunicorn reporthuman.wsgi --env DJANGO_SETTINGS_MODULE=reporthuman.settings.deploy --bind 0.0.0.0:8000"]
