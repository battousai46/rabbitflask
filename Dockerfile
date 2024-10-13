FROM python:3.9-slim


WORKDIR /app

RUN pip install --upgrade pip==23.0.1
ADD requirements.txt .
RUN pip install -r requirements.txt


COPY . /app
CMD ["gunicorn","-w","1","--bind","0.0.0.0:8000","app:create_app()"]