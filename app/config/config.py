from os import getenv


class Config:
    def __init__(self):
        self.app_version = getenv("VERSION")
        self.env = getenv("ENV", "DEV")
        self.redis_host = getenv("REDISTHOST", "")
        self.redis_port = getenv("REDISPORT", "")
        self.celery_broker = getenv("CELERY_BROKER_URL")#f"amqp://{getenv('RABBITMQ_DEFAULT_USER')}:{getenv('RABBITMQ_DEFAULT_PASS')}@rabbitmq"
        print(f"-------worker path-------{self.celery_broker}")


config = Config()

