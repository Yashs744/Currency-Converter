from http.server import HTTPServer
from app import routes

server = HTTPServer(('0.0.0.0', 8000), routes.CurrencyConverterHandler)
print('Starting server at Port 8000')
server.serve_forever()