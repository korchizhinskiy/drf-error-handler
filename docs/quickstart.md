# Quickstart

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

Set the exception handler for all API views
```python
REST_FRAMEWORK = {
    # other settings
    "EXCEPTION_HANDLER": "drf_error_handler.handler.exception_handler"
}
```

or on a view basis (especially if you're introducing this to a versioned API)
```python
from drf_error_handler.handler import exception_handler
from rest_framework.views import APIView

class MyAPIView(APIView):
    def get_exception_handler(self):
        return exception_handler
```

Now, your API error responses for 4xx and 5xx errors, will look like this
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
      "attr": "title"
    }
  ]
}
```

## Integration with DRF spectacular
If you plan to use [drf-spectacular](https://github.com/tfranzel/drf-spectacular) to generate an OpenAPI 3 schema,
install with `pip install drf-error-handler[openapi]`. After that, check the doc page for configuring the
integration.
