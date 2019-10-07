from django.http import JsonResponse
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.views import APIView


class BaseView(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    @staticmethod
    def json_result(code, msg, data):
        res = {'code': code, 'msg': msg, 'data': data}
        return JsonResponse(res)

    @staticmethod
    def error(msg='Error', data=None):
        return BaseView.json_result(500, msg, data)

    @staticmethod
    def ok(msg='Ok', data=None):
        return BaseView.json_result(200, msg, data)

    @staticmethod
    def bad_request(msg='Bad Request', data=None):
        return BaseView.json_result(400, msg, data)

    @staticmethod
    def not_found(msg='Not Found', data=None):
        return BaseView.json_result(404, msg, data)
