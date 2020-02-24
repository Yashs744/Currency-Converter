import json

from app.constants import ErrorCodes
from http import HTTPStatus


def error_response(error_code, status_code, **kwargs):
    """
    Generic method to return error response

    :param error_code: ``ErrorCodes``
        Enum
    :return:
    """

    res = {
        'status': 'failure',
        'error_code': error_code.value,
        'description': error_code.description
    }

    for key, value in kwargs.items():
        res[key] = value

    return json.dumps(res).encode()


def success_response(**kwargs):
    """
    Generic method to return success response
    """

    return json.dumps(kwargs).encode()
