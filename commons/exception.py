from django.utils.deprecation import MiddlewareMixin

from .view import BaseView


class ResponseException(Exception):
    def as_string(self):
        return ','.join(self.args)


class BadRequestException(ResponseException):
    def __init__(self, msg='Bad Request!'):
        super().__init__(msg)


class ServerErrorException(ResponseException):
    def __init__(self, msg='Internal Server Error!'):
        super().__init__(msg)


class NotFoundException(ResponseException):
    def __init__(self, msg='Resource Not Found!'):
        super().__init__(msg)


def to_dict(request):
    return {
        'method': request.method,
        'path': request.path,
        'body': request.body.decode(),
    }


def handler_bad_request(request, ex):
    msg = ex.as_string()
    data = to_dict(request)
    return BaseView.bad_request(msg=msg, data=data)


def handler_server_error(request, ex):
    msg = ex.as_string()
    data = to_dict(request)
    return BaseView.error(msg=msg, data=data)


def handler_not_found(request, ex):
    msg = ex.as_string()
    data = to_dict(request)
    return BaseView.not_found(msg=msg, data=data)


handlers = {
    BadRequestException: handler_bad_request,
    ServerErrorException: handler_server_error,
    NotFoundException: handler_not_found,
}


class ExceptionInterceptorMiddlewareMixin(MiddlewareMixin):
    @staticmethod
    def process_exception(request, ex):
        if isinstance(ex, ResponseException):
            if ex.__class__ in handlers:
                return handlers[ex.__class__](request, ex)
        raise ex
