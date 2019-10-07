from commons.exception import BadRequestException


def exception_view(request):
    raise BadRequestException(msg='abc')
