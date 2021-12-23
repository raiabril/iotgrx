

from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Sensor(Base):
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=255, blank=True)
    external_id = models.CharField(max_length=50, blank=False, primary_key=True)

    def __str__(self):
        return self.external_id


class Event(Base):
    key = models.CharField(max_length=50)
    value = models.FloatField()
    unit = models.CharField(max_length=50)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sensor.external_id} - {self.value} {self.unit}'
