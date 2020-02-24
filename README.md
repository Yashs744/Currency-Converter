# Currency Converter (USD <--> RUB)

- [API Overview](api_overview.md)

## Setup
To start the Currency Converter API server (requirement python3+)

    1. cd Currenct-Converter-Docker/
    2. python application.py

## Docker 

### Setup
To setup docker image

    1. cd Currenct-Converter-Docker/
    2. docker build -t currency-converter .

Executing

    docker run --rm -it -p 8000:8000 currency-converter

This will start the docker image at `localhost:8000` <br>
To stop the server `CTRL + C` 

### Load
Pull the docker container from the docker hub
    
    docker pull yash3498/currencyconverter:latest

Execute

    sudo docker run --rm -it -p 8000:8000 yash3498/currencyconverter

This will start the docker image at `localhost:8000` <br>
To stop the server `CTRL + C`

## Test
Run test by `python -m unittest test.TestingCurrencyConverter`
