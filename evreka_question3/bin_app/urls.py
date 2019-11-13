from django.conf.urls import url
from .views import get_collect_frequency

urlpatterns = [
    url("^$", get_collect_frequency, name="collect_frequency")
]
