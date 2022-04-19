import json

from src.app_lambda import LambdaApp
from src.helpers.http_lambda import HttpRequest, HttpResponse

app = LambdaApp()


@app.add_route(path='/hi', method="GET")
def hello(request, context):
    body = f'Hello {request.query_string_parameters["name"]}'
    return HttpResponse(body=body, status_code=400)


@app.add_route(path='/hello', method="GET")
def hellow(request, context):
    return HttpResponse(body='vai!')

@app.add_route(path='/header', method="POST")
def show_headers(request, context):
    return HttpResponse(body=request.headers)


def lambda_handler(event, context):
    return app(event, context).toDict()

event = {
    "queryStringParameters": {
        "name": "Bruno"
    },
    "requestContext": {
            "http": {
                "method": "GET",
                "path": "/hi",
                "protocol": "HTTP/1.1",
                "sourceIp": "123.123.123.123",
                "userAgent": "agent"
            }
        },
        "body": "Hello from client :) !"
}

print(lambda_handler(event, None))