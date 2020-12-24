FROM python:3.7


COPY . /app

WORKDIR /app

#RUN ls -la
RUN pip install -r requirements.txt

VOLUME . /app/shop

EXPOSE 8000

CMD python manage.py runserver 0:8000