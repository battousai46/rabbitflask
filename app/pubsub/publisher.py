import json
import boto3

local_sqs_url = "http://localhost:4566/000000000000/sqs-flask-queue"
# sqs in localstack
sqs = boto3.resource("sqs", endpoint_url="http://localhost:4566", region_name='ap-southeast-2')


class Publisher:
    def __init__(self):
        self._queue = sqs.Queue(url=local_sqs_url)

    def publish(self, msg):
        try:
            self._queue.send_message(MessageBody=json.dumps(msg))
        except Exception as ex:
            print(f"failing to publish msg in sqs {msg}")

