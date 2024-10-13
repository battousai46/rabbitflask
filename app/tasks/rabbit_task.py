from app.worker import celery_app


@celery_app.task(bind=True, max_retries=5, soft_time_limit=120)
def rabbit_task_exec(self, arg_one, arg_two):
    print(f"---------rabbit task executing----args : {arg_one} {arg_two}")
