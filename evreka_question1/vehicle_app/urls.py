from django.conf.urls import url
from .views import get_last_points

urlpatterns = [
    url('^$', get_last_points, name='last_points')
]
