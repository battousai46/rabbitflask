import signal
from functools import wraps
from time import sleep


def run_till_terminated(backoff_factor=2, max_delay=60):
    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            fail_cnt = 0
            while not TaskRunner.termination_flag:
                try:
                    return func(*args, **kwargs)
                except KeyboardInterrupt:
                    return
                except Exception:
                    fail_cnt += 1
                    delay = min(backoff_factor ** fail_cnt, max_delay)
                    print(f"Exception occurred in task runner, retry delay {delay}")
                    sleep(delay)
            print("shutting down retry_wrapper loop")

        return wrapped


class TaskRunner:
    termination_flag = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.set_termniation_flag)
        signal.signal(signal.SIGTERM, self.set_termination_flag)

    def set_termination_flag(self, *args):
        print("termination of task runner requested")
        termination_flag = True
