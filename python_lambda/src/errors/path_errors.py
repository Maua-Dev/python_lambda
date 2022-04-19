from python_lambda.src.errors.base_error import BaseError


class PathAlreadyExistsError(BaseError):
    """
    Raised when a path already exists.
    """

    def __init__(self, path: str):
        super().__init__(f'Path {path} is already used for this method.')
