import boto3
import json
from app.pubsub.task_runner import run_till_terminated
from app.pubsub.task_runner import TaskRunner as task_runner

local_sqs_url = "http://localhost:4566/000000000000/sqs-flask-queue",
# sqs in localstack
_sqs = boto3.resource("sqs", endpoint_url="http://localhost:4566", region_name='ap-southeast-2')

_queue = _sqs.Queue(url=local_sqs_url)


def get_sqs_msg():
    return _queue.receive_message(
        MaxNumberOfMessages=3,
        VisibilityTimeout=60,
        WaitTimeSeconds=20,
    )


@run_till_terminated()
def process_sqs_msg():
    print("Polling for msg from sqs flask queue")
    for msg in get_sqs_msg():
        try:
            body = json.loads(msg.body)
            print(body)
        except Exception as ex:
            print("failed to process msg from flask sqs q")
        finally:
            msg.delete()

if __name__ == "__main__":
    print("consumer flask sqs initiating")
    while not task_runner.termination_flag:
        process_sqs_msg()
    print("consumer flask sqs terminated")

