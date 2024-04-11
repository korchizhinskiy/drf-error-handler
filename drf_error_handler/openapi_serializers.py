from django.db import models
from rest_framework import serializers


class ValidationErrorEnum(models.TextChoices):
    VALIDATION_ERROR = "validation_error"


class ClientErrorEnum(models.TextChoices):
    CLIENT_ERROR = "client_error"


class ServerErrorEnum(models.TextChoices):
    SERVER_ERROR = "server_error"


class ValidationErrorSerializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField()


class ValidationErrorResponseSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ValidationErrorEnum.choices)
    errors = ValidationErrorSerializer(many=True)


class ParseErrorSerializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField(allow_null=True)


class ParseErrorResponseSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ClientErrorEnum.choices)
    errors = ParseErrorSerializer(many=True)


class Error401Serializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField(allow_null=True)


class ErrorResponse401Serializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ClientErrorEnum.choices)
    errors = Error401Serializer(many=True)


class Error403Serializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField(allow_null=True)


class ErrorResponse403Serializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ClientErrorEnum.choices)
    errors = Error403Serializer(many=True)


class Error404Serializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField(allow_null=True)


class ErrorResponse404Serializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ClientErrorEnum.choices)
    errors = Error404Serializer(many=True)


class Error405Serializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField(allow_null=True)


class ErrorResponse405Serializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ClientErrorEnum.choices)
    errors = Error405Serializer(many=True)


class Error406Serializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField(allow_null=True)


class ErrorResponse406Serializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ClientErrorEnum.choices)
    errors = Error406Serializer(many=True)


class Error415Serializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField(allow_null=True)


class ErrorResponse415Serializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ClientErrorEnum.choices)
    errors = Error415Serializer(many=True)


class Error429Serializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField(allow_null=True)


class ErrorResponse429Serializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ClientErrorEnum.choices)
    errors = Error429Serializer(many=True)


class Error500Serializer(serializers.Serializer):
    detail = serializers.CharField()
    attr = serializers.CharField(allow_null=True, )


class ErrorResponse500Serializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=ServerErrorEnum.choices)
    errors = Error500Serializer(many=True)
