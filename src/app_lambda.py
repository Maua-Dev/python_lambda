from src.helpers.http_lambda import HttpResponse, HttpRequest
from src.errors.path_errors import PathAlreadyExistsError


class LambdaApp:
    """
    This class is the main class of the application.
    """
    paths: dict
    allowed_methods: list = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self):
        self.paths = {x: {} for x in self.allowed_methods}

    def add_route(self, path: str, method: str = 'GET'):
        def wrapper(func):
            if path in self.paths['GET']:
                raise PathAlreadyExistsError(path)
            self.paths['GET'][path] = func

        return wrapper

    def __call__(self, request: HttpRequest, context) -> HttpResponse:
        # checks if path exists
        if request.http.path in self.paths[request.http.method]:
            # calls the function
            return self.paths[request.http.method][request.http.path](request, context)

        return HttpResponse({"status_code": 404, "body": {"message": "Not Found"}})
