FROM python:3.8.3

RUN pip install pipenv
WORKDIR /app
COPY Pipfile* ./
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
COPY ./app ./

ENTRYPOINT [ "uvicorn" ]
CMD ["main:app", "--host", "0.0.0.0", "--reload", "--port", "80"]