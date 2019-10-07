try:
    from RPi import GPIO
except ImportError:
    GPIO = None


def setup():
    if GPIO is None:
        print('Setup GPIO!')
        return
    GPIO.setmode(GPIO.BCM)


def setup_output(pins):
    if GPIO is None:
        print('Set pins [%s] to output!' % pins)
        return
    for pin in pins:
        GPIO.setup(pin, GPIO.OUTPUT)


def read_value(pin):
    if GPIO is None:
        print('Read pin value %s, mock True' % pin)
        return True
    return GPIO.input(pin)


def write_value(pin, value):
    if GPIO is None:
        print('Set pin %s value to %s' % (pin, value))
        return
    if value:
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)
