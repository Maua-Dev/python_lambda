from python_lambda.src.helpers.http_lambda import HttpResponse, HttpRequest
from python_lambda.src.errors.path_errors import PathAlreadyExistsError


class LambdaApp:
    """
    This class is the main class of the application.
    """
    paths: dict
    allowed_methods: list = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self):
        self.paths = {m: {} for m in self.allowed_methods}

    def add_route(self, path: str, method: str = 'GET'):
        def wrapper(func):
            if path in self.paths[method]:
                raise PathAlreadyExistsError(path)
            self.paths[method][path] = func

        return wrapper

    def __call__(self, event) -> HttpResponse:
        # checks if path exists
        request = HttpRequest(event)
        response = HttpResponse()
        if request.http.path in self.paths[request.http.method]:
            # calls the function
            return self.paths[request.http.method][request.http.path](request, response)

        return HttpResponse({"status_code": 404, "body": {"message": "Not Found"}})
