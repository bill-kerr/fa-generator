FROM python:3.8.3

WORKDIR /app
COPY ./app/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./app ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "80"]