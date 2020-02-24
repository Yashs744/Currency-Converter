FROM python:3.7

# Create working directory
WORKDIR /cc-app

# Bundle app source
COPY . /cc-app

# RUN python -m unittest test.TestingCurrencyConverter

EXPOSE 8000
CMD ["python", "application.py"]
