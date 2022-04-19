FROM  amazon/aws-lambda-python:3.9

EXPOSE 8080


COPY python_lambda/src/ ${LAMBDA_TASK_ROOT}/python_lambda/src/


CMD [ "python_lambda.src.example.example.lambda_handler" ]

