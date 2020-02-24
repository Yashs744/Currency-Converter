import json
import logging
import unittest
from app.helpers import get_rate_and_return_response, convert_amount_and_return_response

# disable logging when testing
logging.disable(logging.CRITICAL)

class TestingCurrencyConverter(unittest.TestCase):

    def test_get_method(self):
        """
            Method to test the GET method of Currenct Converter API
        """

        response = get_rate_and_return_response()
        response = json.loads(response.decode())

        assert response["status"] == 'success'
        assert isinstance(response, dict)

    def test_post_method(self):
        """
            Method to test the POST method of Currenct Converter API which converts 
            value of one currency into another USD <-> RUB.
        """

        # Testing condition when no request data is passed
        request_data = None

        response_code, response = convert_amount_and_return_response(request_data)
        response = json.loads(response.decode())

        assert response_code == 405
        assert response['error_code'] == 300

        # Testing condition when request data is empty
        # This differ from the above as here request data is present but is empty (no key:value)
        request_data = json.dumps({})
        response_code, response = convert_amount_and_return_response(request_data)
        response = json.loads(response.decode())

        assert response_code == 400
        assert response['error_code'] == 302

        # Testing condition when incorrect currency type is passed
        request_data = json.dumps({"currency": "EUR", "amount": 1.0})
        response_code, response = convert_amount_and_return_response(request_data)
        response = json.loads(response.decode())

        assert response_code == 400
        assert response['error_code'] == 303

        # Testing condition when incorrect amount type is passed
        request_data = json.dumps({"currency": "USD", "amount": 1})
        response_code, response = convert_amount_and_return_response(request_data)
        response = json.loads(response.decode())

        assert response_code == 400
        assert response['error_code'] == 304

        # Testing condition when correct parameters are passed.
        request_data = json.dumps({"currency": "USD", "amount": 100.0})
        response_code, response = convert_amount_and_return_response(request_data)
        response = json.loads(response.decode())

        assert response_code == 200
        assert response['status'] == 'success'

        request_data = json.dumps({"currency": "RUB", "amount": 100.0})
        response_code, response = convert_amount_and_return_response(request_data)
        response = json.loads(response.decode())

        assert response_code == 200
        assert response['status'] == 'success'
