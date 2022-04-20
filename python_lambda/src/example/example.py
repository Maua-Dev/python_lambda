from python_lambda.src.app_lambda import LambdaApp
from python_lambda.src.helpers.http_lambda import HttpResponse, HttpRequest
import asyncio

app = LambdaApp()


@app.add_route(path='/hi', method="GET")
async def hello(request: HttpRequest, response: HttpResponse):
    body = f'Hello {request.query_string_parameters["name"]}'
    response.body = body
    response.status_code = 400
    return response


@app.add_route(path='/hello', method="GET")
async def hellow(request, response):
    return HttpResponse(body='vai!')

@app.add_route(path='/header', method="POST")
async def show_headers(request, response):
    return HttpResponse(body=request.headers)

@app.add_route(path='/redirect', method="GET")
async def redirect(request, response):
    response.status_code = 302
    response.headers['Location'] = 'https://google.com'
    return response


def lambda_handler(event, context):
    res = app.async_call(event)
    return res.toDict()

event = {
    "queryStringParameters": {
        "name": "Bruno"
    },
    "requestContext": {
            "http": {
                "method": "GET",
                "path": "/hidsa",
                "protocol": "HTTP/1.1",
                "sourceIp": "123.123.123.123",
                "userAgent": "agent"
            }
        },
        "body": "Hello from client :) !"
}

print(lambda_handler(event, None))

# async def main():
#     resp = await
#     print(resp)
#
# asyncio.run(main())