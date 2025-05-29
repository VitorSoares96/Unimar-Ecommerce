FROM python:3.12-alpine

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . .

EXPOSE 8000

CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
ENV debug=1