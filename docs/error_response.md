# Error Response Format

The default error response format looks like this
```json
{
  "type": "validation_error",
  "errors": [
    {
      "detail": "This field is required.",
      "attr": "name"
    }
  ]
}
```

- `type`: can be `validation_error`, `client_error` or `server_error`
- `detail`: User-friendly text describing the error.
- `attr`: set only when the error type is a `validation_error` and maps to the serializer field name or `settings.NON_FIELD_ERRORS_KEY`.

## Error Types

### Validation Errors

These are ones caused by raising a `rest_framework.exceptions.ValidationError`. They are the only error type
that can have more than 1 error. The list of corresponding error codes depends on the serializer and its fields.

### Client Errors

Covers all 4xx errors other than validation errors. Here's a reference to all possible error codes and corresponding exceptions:

| Error Code             | Status Code | DRF Exception                                                                                            |
| ---------------------- | ----------- | -------------------------------------------------------------------------------------------------------- |
| parse_error            | 400         | [ParseError](https://www.django-rest-framework.org/api-guide/exceptions/#parseerror)                     |
| authentication_failed  | 401         | [AuthenticationFailed](https://www.django-rest-framework.org/api-guide/exceptions/#authenticationfailed) |
| not_authenticated      | 401         | [NotAuthenticated](https://www.django-rest-framework.org/api-guide/exceptions/#notauthenticated)         |
| permission_denied      | 403         | [PermissionDenied](https://www.django-rest-framework.org/api-guide/exceptions/#permissiondenied)         |
| not_found              | 404         | [NotFound](https://www.django-rest-framework.org/api-guide/exceptions/#notfound)                         |
| method_not_allowed     | 405         | [MethodNotAllowed](https://www.django-rest-framework.org/api-guide/exceptions/#methodnotallowed)         |
| not_acceptable         | 406         | [NotAcceptable](https://www.django-rest-framework.org/api-guide/exceptions/#notacceptable)               |
| unsupported_media_type | 415         | [UnsupportedMediaType](https://www.django-rest-framework.org/api-guide/exceptions/#unsupportedmediatype) |
| throttled              | 429         | [Throttled](https://www.django-rest-framework.org/api-guide/exceptions/#throttled)                       |

### Server Errors

These are ones caused by raising a `rest_framework.exceptions.APIException` or by unhandled exceptions.
The corresponding error code is `error` and the status code is 500.

## Multiple Errors Support

Out of the box, only validation errors would result in an error response with multiple errors. The errors
can be for the same field or for different fields. So, a sample DRF error dict like this:
```
{
    "phone": [
        ErrorDetail("The phone number entered is not valid.", code="invalid_phone_number")
    ],
    "password": [
        ErrorDetail("This password is too short."),
        ErrorDetail("The password is too similar to the username."),
    ],
}
```
would be converted to:
```json
{
    "type": "validation_error",
    "errors": [
        {
            "detail": "The phone number entered is not valid.",
            "attr": "phone"
        },
        {
            "detail": "This password is too short.",
            "attr": "password"
        },
        {
            "detail": "The password is too similar to the username.",
            "attr": "password"
        }
    ]
}
```

## Nested Serializers Support

Taking this example
```
{
    "shipping_address": {
        "non_field_errors": [ErrorDetail("We do not support shipping to the provided address.")]
    }
}
```
It will be converted to:
```json
{
    "detail": "We do not support shipping to the provided address.",
    "attr": "shipping_address.non_field_errors"
}
```
Note how the `attr` is the combined value of parent serializer field name and nested one. They are separated by
a `.` by default, but that can be changed through the setting `NESTED_FIELD_SEPARATOR`.

## List Serializers Support
This example
```
{
    "recipients": [
        {"name": [ErrorDetail("This field is required.")]},
        {"email": [ErrorDetail("Enter a valid email address.")]},
    ]
}
```
would be converted to
```json
{
    "type": "validation_error",
    "errors": [
        {
            "detail": "This field is required.",
            "attr": "recipients.0.name"
        },
        {
            "detail": "Enter a valid email address.",
            "attr": "recipients.1.email"
        }
    ]
}
```
Note that distinguishing between errors in different objects in the nested list serializer is done using
0-based indexing.
