FROM python:3.7-alpine

WORKDIR /glcm
ENV FLASK_APP=glcm.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV = development
RUN apk add --no-cache gcc musl-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 9000
COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=9000"]
