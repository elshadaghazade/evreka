# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Max, F
from django.db.models.functions import Now
from .models import *
import datetime, time

def get_last_points(request):

    # Following query set gets max datetime of each vehicle
    # This query set is equivalent with: 
    #   SELECT vehicle_id, MAX(datetime) 
    #     FROM navigation_record 
    #    WHERE datetime > CURRENT_TIMESTAMP - INTERVAL 2 days 
    # GROUP BY vehicle_id

    qs1 = NavigationRecord.objects.filter(datetime__gt=Now() - datetime.timedelta(hours=48)).values('vehicle').annotate(v=F('vehicle_id'), m=Max('datetime', distinct=True)).values('m')

    # and we are subquering above query set to get all information
    qs2 = NavigationRecord.objects.distinct('vehicle').filter(datetime__in=qs1).annotate(plate=F('vehicle__plate')).values('plate', 'vehicle_id', 'latitude', 'longitude', 'datetime')
    
    t1 = time.time()
    # with list comprehension method we create list of points to be able to serialize them and send as a json response
    points = [{'vehicle_id': row.get('vehicle_id'), 'vehicle_plate': row.get('plate'), 'datetime': datetime.datetime.strftime(row.get('datetime'), "%d.%m.%Y %H:%M:%S"), 'latitude': row.get('latitude'), 'longitude': row.get('longitude')} for row in qs2]
    t2 = time.time()

    return JsonResponse({
        'result': 'OK',
        'message': 'Looked up through ' + str(NavigationRecord.objects.count()) + ' records along ' + str(t2 - t1) + ' seconds',
        'data': points
    })
