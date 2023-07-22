FROM python:3.9-slim

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser

RUN mkdir -p /app/config
WORKDIR /app

RUN pip install --upgrade pip==23.0.1
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD app /app/app

USER appuser

#CMD ["gunicorn","-w","1","--bind","0.0.0.0:8000","app:create_app()"]