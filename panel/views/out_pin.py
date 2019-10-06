from commons.view import BaseView


def check_create_param(param):
    pass


class OutPinView(BaseView):

    def get(self, request, id):
        return self.ok()

    def put(self, request, ignore):
        print(request.data)
        return self.ok(data=request.data)
