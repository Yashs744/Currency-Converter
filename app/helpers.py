import json
import logging
import traceback

from app.constants import ErrorCodes
from app.responses import error_response, success_response

from datetime import datetime
from http import HTTPStatus
from urllib.request import Request, urlopen
import urllib.error

# Constant
BASE_URL = "https://api.exchangeratesapi.io/latest?symbols=USD,RUB&base={}"


def __fetch_latest_rate__(currency = 'USD'):
    """
        Method to fetch latest exchange rate with the base as `currency`.

        :param: `` currency ``
            str

        :return: `` rates ``
            dict
    """

    req = Request(BASE_URL.format(currency))
    response = urlopen(req)
    
    data = response.read().decode()
    data = json.loads(data)

    return data.get('rates')

def get_rate_and_return_response():
    """
        ``` GET METHOD ```
        Method to fetch latest currency exchange rate and return JSON response.

        :return:
            RESPONSE (SUCCESS OR ERROR)
    """

    rate = 0.0
    try:
        rate = __fetch_latest_rate__()

    except Exception as e:
        print('\nCODE: 101    ' + str(e), flush=True)
        print(traceback.format_exc(), flush=True)
        print(flush=True)

        logging.error(str(e))

        return error_response(error_code=ErrorCodes.UNEXPECTED, status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value)

    rates = {
        "USD": 1.0,
        "RUB": rate
    }

    return success_response(status='success', rates=rates, date=str(datetime.now()))


def convert_amount_and_return_response(request_data):
    """
        ``` POST METHOD ```
        Method to convert amount from USD to RUBLE or from RUBLE to USD and 
        return JSON response.

        :param: ``request_data``
            RAW request body
        
        :return:
            HTTP RESPONSE CODE
            RESPONSE (SUCCESS OR ERROR)
    """

    '''
        Check whether the request data passed to the API is correct or not.
        The if statements make sure that correct data is passed to the API for currency
        conversion. Sanity checks include checking request data is not empty, it contains 
        correct key-value pairs.
    '''
    try:
        data = json.loads(request_data)
    except Exception as e:
        logging.error(str(e))

        return HTTPStatus.METHOD_NOT_ALLOWED.value, error_response(error_code=ErrorCodes.METHOD_NOT_ALLOWED, status_code=HTTPStatus.METHOD_NOT_ALLOWED.value)

    # request data must contain currenct and amount keys.
    if data.get('currency', None) is None or data.get('amount', None) is None:
        logging.error("Parameter missing in the request body")

        return HTTPStatus.BAD_REQUEST.value, error_response(error_code=ErrorCodes.PARAMETER_MISSING, status_code=HTTPStatus.BAD_REQUEST.value)

    # only two currency type are supported US Dollars and Russian RUBLES
    elif str(data['currency']).upper() not in ['USD', 'RUB']:
        logging.error("Invalid currency in the request body")

        return HTTPStatus.BAD_REQUEST.value, error_response(error_code=ErrorCodes.INVALID_CURRENCY, status_code=HTTPStatus.BAD_REQUEST.value)
    
    # currency amount must be float.
    elif not type(data['amount']) == float:
        logging.error("Invalid amount in the request body")

        return HTTPStatus.BAD_REQUEST.value, error_response(error_code=ErrorCodes.INVALID_AMOUNT, status_code=HTTPStatus.BAD_REQUEST.value)

    try:
        currency = data['currency']

        conversion = {
            "currency": currency,
            "USD": 0.0,
            "RUB": 0.0
        }

        rate = __fetch_latest_rate__(currency=currency)

        if currency == 'USD':
            value_in_ruble = float(data['amount'] * rate['RUB'])
            conversion["USD"] = data['amount']
            conversion["RUB"] = value_in_ruble

        else:
            value_in_usd = float(data['amount'] * rate['USD'])
            conversion["USD"] = value_in_usd
            conversion["RUB"] = data['amount']

        logging.info("Currency Conversion")

    except Exception as e:
        print('CODE: 102    ' + str(e), flush=True)
        print(traceback.format_exc(), flush=True)
        print(flush=True)

        logging.error(str(e))

        return HTTPStatus.INTERNAL_SERVER_ERROR.value, error_response(error_code=ErrorCodes.UNEXPECTED, status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value)

    return HTTPStatus.OK.value, success_response(status='success', rates=conversion, date=str(datetime.now()))