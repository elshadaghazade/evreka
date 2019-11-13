import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evreka_question3.settings')

import django; django.setup()

from bin_app.models import *
import random, datetime

operations = []
Operation.objects.all().delete()
for i in range(1, 5):
    operation = Operation()
    operation.name = "operation" + str(i)
    operations.append(operation)

operations = Operation.objects.bulk_create(operations)

bins = []
Bin.objects.all().delete()
for i in range(10):
    bin = Bin()
    bin.latitude = random.random() * 180
    bin.longitude = random.random() * 180
    bins.append(bin)

bins = Bin.objects.bulk_create(bins)

completed_operations = []
OperationLog.objects.all().delete()
dt = datetime.datetime.now() - datetime.timedelta(days=365)

for i in range(10000):
    dt += datetime.timedelta(minutes=random.randint(30, 60))
    operation = OperationLog()
    operation.bin = random.choice(bins)
    operation.operation = random.choice(operations)
    operation.operation_datetime = dt
    operation.save()

