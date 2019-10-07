from django.forms import model_to_dict

from board import gpio
from commons.view import BaseView
from panel.models import MainPower


def get_status(request):
    main_power_pin = MainPower.objects.instance()
    res_table = model_to_dict(main_power_pin)
    res_table['value'] = gpio.read_value(main_power_pin.pin_num)
    return BaseView.ok(data=res_table)


def set_pin_value(request):
    value = request.data['value']
    gpio.write_value(MainPower.objects.instance().pin_num, value)
    return BaseView.ok(data=value)


def set_pin_num(request):
    num = request.data['pin_num']
    if num == '' or not num.isdigit():
        return BaseView.bad_request(msg='invalidate pin num!')
    num = int(num)
    MainPower.objects.set_pin_num(num)
    gpio.setup_output([num])
    return BaseView.ok(data=num)


get_handlers = {
    "": get_status
}

post_handlers = {
    'value': set_pin_value,
    'pin_num': set_pin_num,
}


class MainPowerView(BaseView):
    def get(self, request, operation):
        if operation in get_handlers:
            return get_handlers[operation](request)
        return self.bad_request(msg='Invalidate operation!')

    def post(self, request, operation):
        if operation in post_handlers:
            return post_handlers[operation](request)
        return self.bad_request(msg='Invalidate operation!')
