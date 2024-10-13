from celery import Celery

from pkgutil import iter_modules
from pathlib import Path
from app.config import config


def find_task_modules():
    task_path = [f"{Path().absolute()}/app"]
    task_to_register = [module.name for module in iter_modules(task_path, prefix="app.")]
    print("---task registered---")
    print(task_to_register)
    return task_to_register


celery_app = Celery(__name__, broker=config.celery_broker)
celery_app.autodiscover_tasks(find_task_modules())
print(config.celery_broker)
print(celery_app.conf.broker_read_url)