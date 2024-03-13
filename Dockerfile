FROM python:3.11.7

WORKDIR /usr/app

RUN pip install flask

COPY poetry.lock pyproject.toml main.py /usr/app/

EXPOSE 1234

CMD python main.py