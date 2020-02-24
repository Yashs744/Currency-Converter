# Currency Converter API Overview

- [Schema](#schema)
- [HTTP Responses](#http-responses)
- [Error Codes](#error-codes)
- [API Methods](#api-methods)
  * [Get Exchange Rate](#get-exchange-rate)
  * [Convert Currency](#convert-currency)

## Schema
All data (response) is sent as JSON including error messages.

## HTTP Responses
| Status | Description | Trigger | 
| ------ | ----------- | ----------- | 
| 200 | Request Successful | The request was successfully executed and returned a response. |
| 400 | Bad Request | The request was not executed |  
| 404 | API does not exist | User requested a non existent API. |
| 405 | Method Not Allowed | User accessing the API by unfair means. |
| 500 | Server Error | A server error occurred when processing the request. <br>For functional errors, the server will return an "error_code" in the response. |

## Error Codes
| Code | Description |
| ------ | ----------- |
| 100 | API not found |
| 300 | Method not allowed |
| 301 | Access not allowed |
| 302 | Incomplete parameters in request body |
| 303 | Invalid currency type in request body |
| 304 | Invalid amount in request body |
| 500 | Unexpected error |

## API Methods

### Get Exchange Rate

```http request
GET /
```

This API is responsible for fetching latest currency exchange rate and returning JSON response.

#### Request Parameters

| Parameter | Location |
| --------- | -------- |

#### Responses

| Status | Description |
| ------ | ----------- |
| 200 | Exchange Rate Response |
| 400 | Bad Request |
| 405 | Method Not Allowed |

#### Sample Request / Response

```http request
GET / HTTP/1.1
```

<br/>

```http request
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
    "status": "string",
    "rates": {
        "USD": "float",
        "RUB": {
            "RUB": "float",
            "USD": "float"
        }
    },
    "date": "timestamp"
}
```

### Convert Currency

```http request
POST /convert
```

Convert Currency from either USD to RUB or RUB to USD and return JSON response.

#### Request Parameters

| Parameter | Location | Description | Required |
| --------- | -------- | -------- | -------- |
| currency | body | Base currency to convert (USD or RUB) (string)| Yes |
| amount | body | Amount to Convert (float) | Yes |

#### Responses

| Status | Description |
| ------ | ----------- |
| 200 | Converted Currency |
| 400 | Bad Request |
| 405 | Method Not Allowed |
| 500 | Internal Server Error |

#### Sample Request / Response

```http request
POST /convert HTTP/1.1
```
```http request
{"currency": "string", "amount": "float"}
```

<br/>

```http request
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
    "status": "string",
    "rates": {
        "currency": "string",
        "USD": "float",
        "RUB": "float"
    },
    "date": "timestamp"
}
```


### error_response

```json
{
    "status": "string",
    "error_code": 0,
    "description": "string"
}
```