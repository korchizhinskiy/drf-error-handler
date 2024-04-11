# DRF Standardized Errors

Standardize your [DRF](https://www.django-rest-framework.org/) API error responses.

[![Read the Docs](https://img.shields.io/readthedocs/drf-error-handler)](https://drf-error-handler.readthedocs.io/en/latest/)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/korchizhinskiy/drf-error-handler/tests.yml?branch=main&label=Tests&logo=GitHub)](https://github.com/korchizhinskiy/drf-error-handler/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/korchizhinskiy/drf-error-handler/branch/main/graph/badge.svg?token=JXTTT1KVBR)](https://codecov.io/gh/korchizhinskiy/drf-error-handler)
[![PyPI](https://img.shields.io/pypi/v/drf-error-handler)](https://pypi.org/project/drf-error-handler/)
[![PyPI - License](https://img.shields.io/pypi/l/drf-error-handler)](https://github.com/korchizhinskiy/drf-error-handler/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

By default, the package will convert all API error responses (4xx and 5xx) to the following standardized format:
```json
{
  "type": "validation_error",
  "errors": [
    {
      "code": "required",
      "detail": "This field is required.",
      "attr": "name"
    },
    {
      "code": "max_length",
      "detail": "Ensure this value has at most 100 characters.",
      "attr": "title"
    }
  ]
}
```
```json
{
  "type": "client_error",
  "errors": [
    {
      "code": "authentication_failed",
      "detail": "Incorrect authentication credentials.",
      "attr": null
    }
  ]
}
```
```json
{
  "type": "server_error",
  "errors": [
    {
      "code": "error",
      "detail": "A server error occurred.",
      "attr": null
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

### Notes
- This package is a DRF exception handler, so it standardizes errors that reach a DRF API view. That means it cannot
handle errors that happen at the middleware level for example. To handle those as well, you can customize
the necessary [django error views](https://docs.djangoproject.com/en/dev/topics/http/views/#customizing-error-views).
You can find more about that in [this issue](https://github.com/korchizhinskiy/drf-error-handler/issues/44).

- Standardized error responses when `DEBUG=True` for **unhandled exceptions** are disabled by default. That is
to allow you to get more information out of the traceback. You can enable standardized errors instead with:
```python
DRF_ERROR_HANDLER = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}
```

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
