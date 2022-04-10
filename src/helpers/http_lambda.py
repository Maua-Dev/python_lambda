class HttpResponse:
    """
    A class to represent an HTTP response for lambda URL.
    docs: https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html
    """
    status_code: int = 200
    body: any = {"message": "No response"}
    headers: dict = {"Content-Type": "application/json"}

    def __init__(self, response: any = None) -> None:
        """
        Constructor for HttpResponse.

        Default values are:
            status_code: 200
            body: {"message": "No response"}
            headers: {"content-type": "application/json"}
            isBase64Encoded: False

        Args:
            response:  can be a dict, a string - dict can have status_code (int), body(str or dict) and/or headers (dict)

        """
        if not response:
            return

        if isinstance(response, str):
            self.body = response

        elif isinstance(response, dict):
            self.body = response["body"] if "body" in response else HttpResponse.body
            self.headers = response["headers"] if "headers" in response else HttpResponse.headers
            self.status_code = response["status_code"] if "status_code" in response else HttpResponse.status_code

    def toDict(self) -> dict:
        """
        Returns a dict representation of the HttpResponse.
        Returns:
            {
                'statuCode': int
                'body': str or dict
                'headers': dict
                'isBase64Encoded': bool
            }
        """
        return {
            "statusCode": self.status_code,
            "body": self.body,
            "headers": self.headers,
            "isBase64Encoded": False
        }

    def __repr__(self):
        return (
            f"HttpResponse (status_code={self.status_code}, body={self.body}, headers={self.headers})"
        )


class LambdaHttp:
    method: str
    path: str
    protocol: str
    source_ip: str
    user_agent: str

    def __init__(self, data: dict) -> None:
        """
        Constructor for LambdaHttp.

        Args:
            event: dict - the event passed to the lambda function.

        """
        self.method = data["method"]
        self.path = data["path"]
        self.protocol = data["protocol"]
        self.source_ip = data["sourceIp"]
        self.user_agent = data["userAgent"]

    def __eq__(self, other):
        if not isinstance(other, LambdaHttp):
            return False
        return self.method == other.method and self.path == other.path and self.protocol == other.protocol and self.source_ip == other.source_ip and self.user_agent == other.user_agent


class HttpRequest:
    """
        A class to represent an HTTP request for lambda URL.
        docs: https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html
        """
    version: str
    raw_path: str
    raw_query_string: str
    headers: dict
    query_string_parameters: dict
    request_context: dict
    http: LambdaHttp
    body: any

    def __init__(self, data: dict = None) -> None:
        """
        Constructor for HttpResponse.
        """
        self.version = data.get("version")
        self.raw_path = data.get("rawPath")
        self.raw_query_string = data.get("rawQueryString")
        self.headers = data.get("headers")
        self.query_string_parameters = data.get("queryStringParameters")
        self.request_context = data.get("requestContext")
        self.http = LambdaHttp(self.request_context["http"])
        self.body = data.get("body")

    def __repr__(self):
        return (
            f"HttpRequest (version={self.version}, raw_path={self.raw_path}, raw_query_string={self.raw_query_string}, headers={self.headers}, query_string_parameters={self.query_string_parameters}, request_context={self.request_context}, http={self.http}, body={self.body})"
        )
