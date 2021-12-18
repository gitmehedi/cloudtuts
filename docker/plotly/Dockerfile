FROM python:3.7
WORKDIR /code

ENV FLASK_APP=dash.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8800
COPY . .
CMD ["flask", "run", "--host=0.0.0.0", "--port=8800"]