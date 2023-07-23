from flask import Flask, jsonify

from app.tasks.rabbit_task import rabbit_task_exec
from app.pubsub.publisher import Publisher

def create_app():
    flask_app = Flask(__name__)
    register_routes(flask_app)
    return flask_app


def register_routes(app):
    @app.route("/")
    def hello():
        return jsonify({"Greetings": "Hello World!"})

    @app.route("/rabbit-task")
    def execute_rabbit_task():
        print("initiating rabbit task for celery")
        rabbit_task_exec.apply_async((3, 7), ignore_result=True)
        return jsonify({"rabbit task":"async queued"})

    @app.route("/sqs-push")
    def publish_sqs_msg():
        print("going to publish msg in flash sqs")
        Publisher().publish({"msg":"event pushed from flask app"})
        return jsonify({"sqs flask":"msg published"})