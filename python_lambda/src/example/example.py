import json

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


event = {'version': '2.0', 'routeKey': '$default', 'rawPath': '//login', 'rawQueryString': '',
         'headers': {'access-control-allow-origin': '*', 'x-amzn-trace-id': 'Root=1-625f5966-63a09b784b0426bd4162f14c',
                     'x-forwarded-proto': 'https', 'postman-token': 'de124314-0439-4cdc-8ce1-2b15696fdc98',
                     'host': 'cgyguxiiuzmblnr25gottz726y0woqyz.lambda-url.sa-east-1.on.aws', 'x-forwarded-port': '443',
                     'content-type': 'application/json', 'x-forwarded-for': '179.110.11.38',
                     'accept-encoding': 'gzip, deflate, br', 'accept': 'application/json',
                     'user-agent': 'PostmanRuntime/7.29.0'},
         'requestContext': {'accountId': 'anonymous', 'apiId': 'cgyguxiiuzmblnr25gottz726y0woqyz',
                            'domainName': 'cgyguxiiuzmblnr25gottz726y0woqyz.lambda-url.sa-east-1.on.aws',
                            'domainPrefix': 'cgyguxiiuzmblnr25gottz726y0woqyz',
                            'http': {'method': 'POST', 'path': '/login', 'protocol': 'HTTP/1.1',
                                     'sourceIp': '179.110.11.38', 'userAgent': 'PostmanRuntime/7.29.0'},
                            'requestId': '1ddffde3-76cd-437e-8b04-2a7705506cac', 'routeKey': '$default',
                            'stage': '$default', 'time': '20/Apr/2022:00:52:54 +0000', 'timeEpoch': 1650415974055},
         'body': '{\r\n    "login": "19.00331-5@maua.br",\r\n    "password": "Teste123!"\r\n}',
         'isBase64Encoded': False}

print(lambda_handler(event, None))

# async def main():
#     resp = await
#     print(resp)
#
# asyncio.run(main())
