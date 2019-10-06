from django.forms import model_to_dict
from django.shortcuts import render

from board import gpio
from commons.view import BaseView
from panel.models import OutPin


def check_create_param(param):
    pass


def all_pins(request):
    all_pin = OutPin.objects.all()
    return render(request, 'panel/setting.html', {'pins': all_pin})


def control_panel(request):
    all_pin = OutPin.objects.all()
    return render(request, 'panel/control-panel.html', {'pins': all_pin})


def sync_pins_mode():
    pins = OutPin.objects.all()
    gpio.setup()
    pin_nums = [pin.pin_num for pin in pins]
    gpio.setup_output(pin_nums)
    return len(pins)


get_handlers = {
    'all': all_pins,
    'panel': control_panel,
}


def read_pin_value(pin):
    return gpio.read_value(pin)


class OutPinView(BaseView):

    def get(self, request, operation):
        if operation in get_handlers:
            return get_handlers[operation](request)
        elif operation.isdigit():
            pin_id = int(operation)
            pin = OutPin.objects.filter(id=pin_id)
            if not len(pin) == 1:
                return self.bad_request('Invalidate query set length %s' % len(pin))
            pin = pin[0]
            value = read_pin_value(pin.pin_num)
            pin_res = model_to_dict(pin)
            pin_res['value'] = value
            return self.ok(data=pin_res)
        else:
            return self.bad_request(msg='Unknown operation!')

    def put(self, request, *args):
        request_data = request.data
        name = request_data['name']
        pin_num = request_data['pin_num']
        description = request_data['description']
        res = OutPin.objects.create(name=name, pin_num=pin_num, description=description)
        model_dict = model_to_dict(res)
        return self.ok(data=model_dict)

    def delete(self, request, delete_id):
        delete_id = int(delete_id)
        res = OutPin.objects.filter(id=delete_id).delete()
        return self.ok(data=res)

    def post(self, request, operation):
        if operation == 'sync':
            size = sync_pins_mode()
            return self.ok(data=size)
        else:
            return self.ok()
