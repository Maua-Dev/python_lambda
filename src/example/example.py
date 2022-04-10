import json

from src.app_lambda import LambdaApp
from src.helpers.http_lambda import HttpRequest, HttpResponse

app = LambdaApp()


@app.add_route(path='/hi', method="GET")
def hello(request, context):
    return HttpResponse(body=request.body, status_code=400)


@app.add_route(path='/hello', method="GET")
def hellow(request, context):
    return HttpResponse(body='vai!')


def lambda_handler(event, context):
    # print(event)
    request = HttpRequest(event)
    return app(request, context).toDict()


event = {
    "requestContext": {
        "http": {
            "method": "GET",
            "path": "/hello",
            "protocol": "HTTP/1.1",
            "sourceIp": "123.123.123.123",
            "userAgent": "agent",
        }
    },
    "body": "Hello from client!!",
}


# context = "LambdaContext([aws_request_id=0ad17140-124d-40ad-9667-5aa7a4257c97,log_group_name=/aws/lambda/Functions,log_stream_name=$LATEST,function_name=test_function,memory_limit_in_mb=3008,function_version=$LATEST,invoked_function_arn=arn:aws:lambda:us-east-1:012345678912:function:test_function,client_context=None,identity=CognitoIdentity([cognito_identity_id=None,cognito_identity_pool_id=None])])"
#
# print(lambda_handler(event, context))
