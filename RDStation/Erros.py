class BaseError(Exception):
    pass


class BadRequestError(BaseError):
    '''400 Bad Request: Malformed body request'''
    pass


class UnauthorizedError(BaseError):
    '''401 Unauthorized: Unauthorized request'''
    pass


class NotFoundError(BaseError):
    '''404 Not Found: Resource Not Found'''
    pass


class TooManyRequestsError(BaseError):
    '''429 Too Many Requests: API usage limit exceeded'''
    pass


class UnprocessableEntityError(BaseError):
    '''422 Unprocessable Entity: Invalid Data type'''
    pass


class InternalServerError(BaseError):
    '''500 Internal Server Error: Service temporarily unavailable'''
    pass