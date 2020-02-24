import json
import logging
import sys

from app.constants import ErrorCodes
from app.helpers import get_rate_and_return_response, convert_amount_and_return_response
from app.responses import error_response, success_response 

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

# Initialize Logger
logging.basicConfig(
    stream=sys.stdout, 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class CurrencyConverterHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        """
            API GET Method
        """

        parsed_path = urlparse(self.path)
        if not parsed_path.path == '/':
            self.send_response(HTTPStatus.NOT_FOUND.value)
            self.end_headers()

            logging.error("Illegal access to API: URL Path " + str(parsed_path.path))
            
            self.wfile.write(error_response(error_code=ErrorCodes.API_NOT_FOUND, status_code=HTTPStatus.NOT_FOUND.value))

            return
        
        self.send_response(HTTPStatus.OK.value)
        self.end_headers()

        logging.info("Success Response")

        self.wfile.write(get_rate_and_return_response())
        
        return

    def do_POST(self):
        """
            API POST Method for currency conversion.
        """

        parsed_path = urlparse(self.path)
        if not parsed_path.path == '/convert':
            self.send_response(HTTPStatus.NOT_FOUND.value)
            self.end_headers()

            logging.error("Illegal access to API: URL Path " + str(parsed_path.path))

            self.wfile.write(error_response(error_code=ErrorCodes.API_NOT_FOUND, status_code=HTTPStatus.NOT_FOUND.value))

            return

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = body.decode("utf-8")

        response_code, response = convert_amount_and_return_response(request_data = data)
            
        self.send_response(response_code)
        self.end_headers()

        self.wfile.write(response)
        
        return