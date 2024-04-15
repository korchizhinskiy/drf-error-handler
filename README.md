# DRF Standardized Errors

Standardize your [DRF](https://www.django-rest-framework.org/) API error responses.

[![Read the Docs](https://img.shields.io/readthedocs/drf-error-handler)](https://drf-error-handler.readthedocs.io/en/latest/)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/korchizhinskiy/drf-error-handler/tests.yml?branch=main&label=Tests&logo=GitHub)](https://github.com/korchizhinskiy/drf-error-handler/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/korchizhinskiy/drf-error-handler/branch/main/graph/badge.svg?token=JXTTT1KVBR)](https://codecov.io/gh/korchizhinskiy/drf-error-handler)
[![PyPI](https://img.shields.io/pypi/v/drf-error-handler)](https://pypi.org/project/drf-error-handler/)
[![PyPI - License](https://img.shields.io/pypi/l/drf-error-handler)](https://github.com/korchizhinskiy/drf-error-handler/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

By default, the package will convert API error responses (4xx) to the following standardized format:
```json
{
  "type": "validation_error",
  "errors": [
    {
      "detail": "This field is required.",
      "attr": "name"
    },
    {
      "detail": "Ensure this value has at most 100 characters.",
      "attr": "title",
      "b_code": 10000
    }
  ]
}
```
```json
{
  "type": "client_error",
  "errors": [
    {
      "detail": "Incorrect authentication credentials.",
      "attr": null,
      "b_code": 11111
    }
  ]
}
```


## Features

- Highly customizable: gives you flexibility to define your own standardized error responses and override
specific aspects the exception handling process without having to rewrite everything.
- Supports nested serializers and ListSerializer errors
- Plays nicely with error monitoring tools (like Sentry, ...)


## Requirements

- python >= 3.8
- Django >= 3.2
- DRF >= 3.12


## Quickstart

Install with `pip`
```shell
pip install drf-error-handler
```

Add drf-error-handler to your installed apps
```python
INSTALLED_APPS = [
    # other apps
    "drf_error_handler",
]
```

Register the exception handler
```python
REST_FRAMEWORK = {
    # other settings
    "EXCEPTION_HANDLER": "drf_error_handler.handler.exception_handler"
}
```
Then you may override something a few settings for package

```python
DRF_ERROR_HANDLER = {
    "EXCEPTION_RESPONSE_BUSINESS_ATTRIBUTE": "b_code"
}
```
This settings define, which attribute will be viewed in response body for business code.
But after that, all exception classes must containt an attribute with name, which you override in `EXCEPTION_RESPONSE_BUSINESS_ATTRIBUTE` settings ("b_code" by default).

For standart DRF Exceptions defined business code in settings.
```python
DRF_ERROR_HANDLER = {
    "VALIDATION_ERROR_BUSINESS_STATUS_CODE": 1001,
    "PARSE_ERROR_BUSINESS_STATUS_CODE": 1002,
    "AUTHENTICATION_FAILED_BUSINESS_STATUS_CODE": 1003,
    "NOT_AUTHENTICATION_BUSINESS_STATUS_CODE": 1004,
    "PERMISSION_DENIED_BUSINESS_STATUS_CODE": 1005,
    "NOT_FOUND_BUSINESS_STATUS_CODE": 1006,
    "METHOD_NOT_ALLOWED_BUSINESS_STATUS_CODE": 1007,
    "NOT_ACCEPTABLE_BUSINESS_STATUS_CODE": 1008,
    "UNSUPPORTED_MEDIA_TYPE_BUSINESS_STATUS_CODE": 1009,
    "THROTTLED_BUSINESS_STATUS_CODE": 1010
}
```
This codes will view for standart DRF and Django exceptions after handle by ErrorHandler in response body.

For create custom exception class, you should do that:
1. Create exception class with inherit from `rest_framework.exceptions.APIException`
```python
from rest_framework.exceptions import APIException

class CustomException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'You can\'t place an order at this time.'
    b_code = 1011

```
You must define b_code (or overriding attribute) in exception class.

2. Raise custom exception.
```python
def view(request):
    ...
    raise CustomException
```

3. And Error Handler process this exception and return valid response.

```json
{
  "type": "client_error",
  "errors": [
    {
      "detail": "You can't place an order at this time.",
      "attr": null,
      "b_code": 1011
    }
  ]
}
```


### Notes
- This package is a DRF exception handler, so it standardizes errors that reach a DRF API view. That means it cannot
handle errors that happen at the middleware level for example. To handle those as well, you can customize
the necessary [django error views](https://docs.djangoproject.com/en/dev/topics/http/views/#customizing-error-views).
You can find more about that in [this issue](https://github.com/korchizhinskiy/drf-error-handler/issues/44).

## Integration with DRF spectacular
If you plan to use [drf-spectacular](https://github.com/tfranzel/drf-spectacular) to generate an OpenAPI 3 schema,
install with `pip install drf-error-handler[openapi]`. After that, check the [doc page](https://drf-error-handler.readthedocs.io/en/latest/openapi.html)
for configuring the integration.

## Links

- Documentation: https://drf-error-handler.readthedocs.io/en/latest/
- Changelog: https://github.com/korchizhinskiy/drf-error-handler/releases
- Code & issues: https://github.com/korchizhinskiy/drf-error-handler
- PyPI: https://pypi.org/project/drf-error-handler/


## License

This project is [MIT licensed](LICENSE).
