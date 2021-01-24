FROM python:3.9.0

WORKDIR /home/

RUN echo "update.20.12/25:lottoapp"
RUN echo "update.20.12/30:points"
RUN echo "update.21.1/15:points"
RUN echo "update.21.1/24:defencegame_update_1st"
RUN echo "update.21.1/24:defencegame_update_1st_fix1"
RUN echo "update.21.1/24:defencegame_update_1st_fix2"
RUN echo "update.21.1/24:defencegame_update_1st_fix3"
RUN echo "update.21.1/24:defencegame_update_1st_fix4"

RUN git clone https://github.com/minkwan4/reporthuman.git



WORKDIR /home/reporthuman/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=reporthuman.settings.deploy && python manage.py migrate --settings=reporthuman.settings.deploy && gunicorn reporthuman.wsgi --env DJANGO_SETTINGS_MODULE=reporthuman.settings.deploy --bind 0.0.0.0:8000"]
