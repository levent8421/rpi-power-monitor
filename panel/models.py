from django.db import models


# Create your models here.
class OutPin(models.Model):
    name = models.CharField(name='name', max_length=255, null=False)
    pin_num = models.IntegerField(name="pin_num", null=False)
    description = models.TextField(name="description")


class MainPowerManager(models.Manager):
    def instance(self):
        power_pin = self.all().first()
        if power_pin:
            return power_pin
        return self.create(pin_num=1)

    def set_pin_num(self, pin_num):
        main_power_pin = self.instance()
        main_power_pin.pin_num = pin_num
        main_power_pin.save()


class MainPower(models.Model):
    pin_num = models.IntegerField(name="pin_num", null=False)
    objects = MainPowerManager()
