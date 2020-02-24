from enum import IntEnum, unique

@unique
class ErrorCodes(IntEnum):
    """Store different error codes."""

    def __new__(cls, value, description):
        obj = int.__new__(cls, value)

        obj._value_ = value
        obj.description = description

        return obj

    API_NOT_FOUND = (100, 'API not found')

    METHOD_NOT_ALLOWED = (300, 'Method not allowed')
    ACCESS_NOT_ALLOWED = (301, 'Access not allowed')

    PARAMETER_MISSING = (302, 'Incomplete parameters in request body')
    INVALID_CURRENCY = (303, 'Invalid currency type in request body')
    INVALID_AMOUNT = (304, 'Invalid amount in request body')

    UNEXPECTED = (500, 'Unexpected error')