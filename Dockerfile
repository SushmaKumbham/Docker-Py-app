# Dockerfile



FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app

COPY app.py .
COPY IF.txt .
COPY Limerick.txt .

#CMD [ "python", "app.py" ]
CMD [ "sh", "-c", "python /app/app.py && cat /app/result.txt" ]


