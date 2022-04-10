import json
import unittest

from src.helpers.http_lambda import HttpRequest, LambdaDefaultHTTP


class TestHttpRequest(unittest.TestCase):
    json_valid_request = """
        {
          "version": "2.0",
          "routeKey": "$default",
          "rawPath": "/my/path",
          "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
          "cookies": [
            "cookie1",
            "cookie2"
          ],
          "headers": {
            "header1": "value1",
            "header2": "value1,value2"
          },
          "queryStringParameters": {
            "parameter1": "value1,value2",
            "parameter2": "value"
          },
          "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": null,
            "authorizer": {
                "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": null,
                        "principalOrgId": null,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
                }
            },
            "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
            "domainPrefix": "<url-id>",
            "http": {
              "method": "POST",
              "path": "/my/path",
              "protocol": "HTTP/1.1",
              "sourceIp": "123.123.123.123",
              "userAgent": "agent"
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390
          },
          "body": "Hello from client!",
          "pathParameters": null,
          "isBase64Encoded": false,
          "stageVariables": null
        }
    """

    def test_valid_request(self):
        json_parsed_request = json.loads(TestHttpRequest.json_valid_request)
        http_request = HttpRequest(json_parsed_request)
        assert http_request.version == "2.0"
        assert http_request.raw_path == "/my/path"
        assert http_request.raw_query_string == "parameter1=value1&parameter1=value2&parameter2=value"
        assert http_request.headers == {"header1": "value1", "header2": "value1,value2"}
        assert http_request.query_string_parameters == {"parameter1": "value1,value2","parameter2": "value"}
        assert http_request.request_context == {"accountId": "123456789012", "apiId": "<urlid>", "authentication": None, "authorizer": { "iam": { "accessKey": "AKIA...", "accountId": "111122223333", "callerId": "AIDA...", "cognitoIdentity": None, "principalOrgId": None, "userArn": "arn:aws:iam::111122223333:user/example-user", "userId": "AIDA..." } }, "domainName": "<url-id>.lambda-url.us-west-2.on.aws", "domainPrefix": "<url-id>", "http": { "method": "POST", "path": "/my/path", "protocol": "HTTP/1.1", "sourceIp": "123.123.123.123", "userAgent": "agent" }, "requestId": "id", "routeKey": "$default", "stage": "$default", "time": "12/Mar/2020:19:03:58 +0000", "timeEpoch": 1583348638390 }
        assert http_request.http == LambdaDefaultHTTP({
            "method": "POST",
            "path": "/my/path",
            "protocol": "HTTP/1.1",
            "sourceIp": "123.123.123.123",
            "userAgent": "agent"
        })
        assert http_request.body == "Hello from client!"


if __name__ == '__main__':
    unittest.main()
