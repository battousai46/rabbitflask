run-dev:
    pip install --upgrade pip && \
	pip install -r requirements.txt && \
	docker-compose up -d && \
 	echo "Waiting for localstack to start up sqs s3" && \
	sleep 10 && \
	$(MAKE) setup-local-sqs

setup-local-sqs:
	awslocal sqs create-queue --region ap-southeast-2 --queue-name sqs-flask-queue

purge-local-sqs:
	awslocal sqs purge-queue --region ap-southeast-2 --queue-name sqs-flask-queue
