from django.db import models


# Create your models here.
class OutPin(models.Model):
    name = models.CharField(name='name', max_length=255, null=False)
    pin_num = models.IntegerField(name="pin_num", null=False)
    description = models.TextField(name="description")
