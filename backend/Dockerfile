FROM python:3.6

RUN mkdir /code
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]