from django.forms import model_to_dict
from django.shortcuts import render

from board import gpio
from commons.view import BaseView
from panel.models import OutPin, MainPower


def check_create_param(param):
    pass


def all_pins(request):
    all_pin = OutPin.objects.all()
    return render(request, 'panel/setting.html', {'pins': all_pin})


def control_panel(request):
    all_pin = OutPin.objects.all()
    for pin in all_pin:
        pin_num = pin.pin_num
        value = gpio.read_value(pin_num)
        pin.value = value
    return render(request, 'panel/control-panel.html', {'pins': all_pin})


def sync_pins_mode(*args):
    pins = OutPin.objects.all()
    gpio.setup()
    pin_nums = [pin.pin_num for pin in pins]
    pin_nums.append(MainPower.objects.instance().pin_num)
    gpio.setup_output(pin_nums)
    return BaseView.ok(data=len(pins))


def set_pin_value(request):
    data = request.data
    pin_id = data['id']
    value = data['value']
    rset = OutPin.objects.filter(id=pin_id)
    if not len(rset) == 1:
        return BaseView.not_found(msg='Pin for id not found!')
    pin = rset[0]
    gpio.write_value(pin.pin_num, value)
    return BaseView.ok(data=value)


get_handlers = {
    'all': all_pins,
    'panel': control_panel,
}
post_handlers = {
    'sync': sync_pins_mode,
    'value': set_pin_value,
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
        pin_num = int(request_data['pin_num'])
        description = request_data['description']
        res = OutPin.objects.create(name=name, pin_num=pin_num, description=description)
        model_dict = model_to_dict(res)
        gpio.setup_output([pin_num])
        return self.ok(data=model_dict)

    def delete(self, request, delete_id):
        delete_id = int(delete_id)
        res = OutPin.objects.filter(id=delete_id).delete()
        return self.ok(data=res)

    def post(self, request, operation):
        if operation in post_handlers:
            return post_handlers[operation](request)
        return self.bad_request(msg='Unknown operation!')
