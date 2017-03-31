FROM python:3.6

ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]