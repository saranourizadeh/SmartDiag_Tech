  FROM python:3.10-buster

  WORKDIR /prod
  COPY requirements.txt requirements.txt

  RUN pip install -r requirements.txt

  COPY app app

  COPY setup.py setup.py
  RUN pip install .

  COPY Makefile Makefile


  CMD uvicorn app.interface.util:app --host 0.0.0.0 --port $PORT
