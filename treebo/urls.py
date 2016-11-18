from django.conf.urls import url
from django.contrib import admin

from treeboapp.views import subscribe, unsubscribe,priceDataPoint

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^subscribe/$', subscribe, name="subscribe"),
    url(r'^unsubscribe/$', unsubscribe, name="unsubscribe"),
    url(r'^dataprice/$', priceDataPoint, name="priceDataPoint"),


]
