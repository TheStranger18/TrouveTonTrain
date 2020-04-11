FROM python:2.7-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt --no-cache-dir

RUN cp flask-spyne.py /usr/local/lib/python2.7/site-packages/flask_spyne/flask_spyne.py

CMD python app.py

EXPOSE 5000