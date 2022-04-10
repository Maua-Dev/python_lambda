FROM  amazon/aws-lambda-python:3.9

EXPOSE 8080


COPY src/ ${LAMBDA_TASK_ROOT}


CMD [ "app_lambda.lambda_handler" ]

