from python_lambda.src.app_lambda import LambdaApp
from python_lambda.src.helpers.http_lambda import HttpResponse, HttpRequest

app = LambdaApp()


@app.add_route(path='/hi', method="GET")
def hello(request: HttpRequest, response: HttpResponse):
    body = f'Hello {request.query_string_parameters["name"]}'
    response.body = body
    response.status_code = 400
    return response


@app.add_route(path='/hello', method="GET")
def hellow(request, response):
    return HttpResponse(body='vai!')

@app.add_route(path='/header', method="POST")
def show_headers(request, response):
    return HttpResponse(body=request.headers)


def lambda_handler(event, context):
    return app(event).toDict()

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