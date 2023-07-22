from celery import Celery
from app.config import config
from pkgutil import iter_modules
from pathlib import Path


def find_task_modules():
    task_path = [f"{Path().absolute()}/app"]
    task_to_register = [module.name for module in iter_modules(task_path, prefix="app.")]
    print(task_to_register)
    return task_to_register


celery_app = Celery(__name__, broker=config.celery_broker)
celery_app.autodiscover_tasks(find_task_modules())
