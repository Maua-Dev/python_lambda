from src.helpers.http_lambda import HttpResponse
from src.errors.path_errors import PathAlreadyExistsError


class LambdaApp:
    paths: dict

    def __init__(self):
        self.paths = {
            'GET': {},
            'POST': {},
            'UPDATE': {},
            'DELETE': {},
        }

    def get(self, path):
        def wrapper(func):
            if path in self.paths['GET']:
                raise PathAlreadyExistsError(path)
            self.paths['GET'][path] = func
        return wrapper

    def __call__(self, event, context):
        self.paths[event['httpMethod']][event['rawPath']](event, context)


        for path in self.paths:
            if event["rawPath"] == path["path"]:
                return HttpResponse(path["func"]()).toDict()
        return HttpResponse({"status_code": 404, "body": {"message": "Not Found"}}).toDict()
