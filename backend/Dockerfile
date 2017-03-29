FROM python:3.6

RUN mkdir /src
WORKDIR /src
ADD . /src
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "-u", "/src/app.py"]