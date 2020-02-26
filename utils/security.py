from functools import wraps


def secure():
    @wraps
    def wrapper(*args, **kwargs):
        # call method to verify Token.
        verify_token()


def verify_token():
    pass
