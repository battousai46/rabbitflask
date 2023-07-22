from flask import Flask, jsonify

from app.tasks.rabbit_task import rabbit_task_exec


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
