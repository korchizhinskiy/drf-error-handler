SECRET_KEY = "some_secret_key"

USE_TZ = True

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "rest_framework",
    "drf_error_handler",
    "tests",
)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

MIDDLEWARE_CLASSES = ("django.middleware.common.CommonMiddleware",)

PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)

ROOT_URLCONF = "tests.urls"

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "drf_error_handler.handler.exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_SCHEMA_CLASS": "drf_error_handler.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "API",
    "DESCRIPTION": "Amazing API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "ENUM_NAME_OVERRIDES": {
        "ValidationErrorEnum": "drf_error_handler.openapi_serializers.ValidationErrorEnum.choices",
        "ClientErrorEnum": "drf_error_handler.openapi_serializers.ClientErrorEnum.choices",
        "ServerErrorEnum": "drf_error_handler.openapi_serializers.ServerErrorEnum.choices",
        "ErrorCode401Enum": "drf_error_handler.openapi_serializers.ErrorCode401Enum.choices",
        "ErrorCode403Enum": "drf_error_handler.openapi_serializers.ErrorCode403Enum.choices",
        "ErrorCode404Enum": "drf_error_handler.openapi_serializers.ErrorCode404Enum.choices",
        "ErrorCode405Enum": "drf_error_handler.openapi_serializers.ErrorCode405Enum.choices",
        "ErrorCode406Enum": "drf_error_handler.openapi_serializers.ErrorCode406Enum.choices",
        "ErrorCode415Enum": "drf_error_handler.openapi_serializers.ErrorCode415Enum.choices",
        "ErrorCode429Enum": "drf_error_handler.openapi_serializers.ErrorCode429Enum.choices",
        "ErrorCode500Enum": "drf_error_handler.openapi_serializers.ErrorCode500Enum.choices",
    },
    "POSTPROCESSING_HOOKS": ["drf_error_handler.openapi_hooks.postprocess_schema_enums"],
}
