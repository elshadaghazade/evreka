# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from .models import BinOperationRel

def get_collect_frequency(request):
    qs = BinOperationRel.objects.all()
    data = [{
        "bin_location": str(row.bin.longitude) + "," + str(row.bin.latitude),
        "operation": row.operation.name,
        "collection_frequency": row.collection_frequency,
        "last_collection": row.last_collection
    } for row in qs]

    return JsonResponse({
        "result": "OK",
        "data": data
    })
