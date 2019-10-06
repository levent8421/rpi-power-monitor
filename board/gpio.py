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
