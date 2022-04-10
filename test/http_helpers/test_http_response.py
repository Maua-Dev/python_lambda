import json
import unittest

from src.helpers.http_lambda import HttpResponse


class TestHttpResponse(unittest.TestCase):

    valid_response_data = {
        "status_code": 201,
        "headers": {
            "Content-Type": "application/json",
            "My-Custom-Header": "Custom Value"
        },
        "body": '{ "message": "Hello, world!" }'
    }




    def test_valid_str_response(self):
        response = HttpResponse(body="Hello, world!")
        expected_response = {
           "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": "Hello, world!",
            "isBase64Encoded": False
        }
        assert response.toDict() == expected_response

    def test_valid_response(self):
        response = HttpResponse(**self.valid_response_data)
        expected_response = {
           "statusCode": 201,
            "headers": {
                "Content-Type": "application/json",
                "My-Custom-Header": "Custom Value"
            },
            "body": "{ \"message\": \"Hello, world!\" }",
            "isBase64Encoded": False
        }
        assert response.toDict() == expected_response



if __name__ == '__main__':
    unittest.main()
