from drf_error_handler.settings import DEFAULTS, IMPORT_STRINGS, PackageSettings
from rest_framework.exceptions import AuthenticationFailed as _AuthenticationFailed
from rest_framework.exceptions import MethodNotAllowed as _MethodNotAllowed
from rest_framework.exceptions import NotAcceptable as _NotAcceptable
from rest_framework.exceptions import NotAuthenticated as _NotAuthenticated
from rest_framework.exceptions import NotFound as _NotFound
from rest_framework.exceptions import ParseError as _ParseError
from rest_framework.exceptions import PermissionDenied as _PermissionDenied
from rest_framework.exceptions import Throttled as _Throttled
from rest_framework.exceptions import UnsupportedMediaType as _UnsupportedMediaType
from rest_framework.exceptions import ValidationError as _ValidationError

package_settings = PackageSettings(DEFAULTS, IMPORT_STRINGS)

B_CODE_ATTRIBUTE = package_settings.EXCEPTION_RESPONSE_BUSINESS_ATTRIBUTE


class ValidationError(_ValidationError):
    def __init__(self, detail=None, code=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.VALIDATION_ERROR_BUSINESS_STATUS_CODE)
        super().__init__(detail, code)


class ParseError(_ParseError):
    def __init__(self, detail=None, code=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.PARSE_ERROR_BUSINESS_STATUS_CODE)
        super().__init__(detail, code)


class AuthenticationFailed(_AuthenticationFailed):
    def __init__(self, detail=None, code=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.AUTHENTICATION_FAILED_BUSINESS_STATUS_CODE)
        super().__init__(detail, code)


class NotAuthenticated(_NotAuthenticated):
    def __init__(self, detail=None, code=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.NOT_AUTHENTICATION_BUSINESS_STATUS_CODE)
        super().__init__(detail, code)


class PermissionDenied(_PermissionDenied):
    def __init__(self, detail=None, code=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.PERMISSION_DENIED_BUSINESS_STATUS_CODE)
        super().__init__(detail, code)


class NotFound(_NotFound):
    def __init__(self, detail=None, code=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.NOT_FOUND_BUSINESS_STATUS_CODE)
        super().__init__(detail, code)


class MethodNotAllowed(_MethodNotAllowed):
    def __init__(self, method, detail=None, code=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.METHOD_NOT_ALLOWED_BUSINESS_STATUS_CODE)
        super().__init__(method, detail, code)


class NotAcceptable(_NotAcceptable):
    def __init__(self, detail=None, code=None, available_renderers=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.NOT_ACCEPTABLE_BUSINESS_STATUS_CODE)
        super().__init__(detail, code, available_renderers)


class UnsupportedMediaType(_UnsupportedMediaType):
    def __init__(self, media_type, detail=None, code=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.UNSUPPORTED_MEDIA_TYPE_BUSINESS_STATUS_CODE)
        super().__init__(media_type, detail, code)


class Throttled(_Throttled):
    def __init__(self, detail=None, code=None):
        setattr(self, B_CODE_ATTRIBUTE, package_settings.THROTTLED_BUSINESS_STATUS_CODE)
        super().__init__(detail, code)
