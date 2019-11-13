from django.db import models
from django.db.models.signals import post_save
from django.db.models import F
import datetime

class Bin(models.Model):
    latitude = models.DecimalField(max_digits=30, decimal_places=27)
    longitude = models.DecimalField(max_digits=30, decimal_places=27)
    operation = models.ManyToManyField('Operation', through='BinOperationRel')

    def __str__(self):
        return "lat-{0:.4f}, lng-{0:.4f}".format(self.latitude, self.longitude)

class Operation(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return "{}".format(self.name)


class BinOperationRel(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    collection_frequency = models.IntegerField(default=0)
    last_collection = models.DateTimeField(null=True)

    def __str__(self):
        return "BIN: {} | OPER: {} | COL-FREQ: {}; LAST-COL: {}".format(self.bin, self.operation, self.collection_frequency, datetime.datetime.strftime(self.last_collection, "%d %b %Y, %H:%M:%S"))

class OperationLog(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    operation_datetime = models.DateTimeField()

    def __str__(self):
        return "BIN: {} | OPER: {} | OPER-DTIME: {}".format(self.bin, self.operation, self.operation_datetime)


def update_bin_operation_rel(sender, **kwargs):
    if kwargs['created']:
        instance = kwargs['instance']

        operation, done = BinOperationRel.objects.get_or_create(bin=instance.bin, operation=instance.operation)

        operation.last_collection = instance.operation_datetime
        operation.collection_frequency += 1
        operation.save()


post_save.connect(update_bin_operation_rel, sender=OperationLog)

