from django.conf.urls import url
from django.views.generic import TemplateView

from .views import index, search, results

app_name = 'indeed_api'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^search/$', search, name='search'),
    url(r'^results/$', results, name='results'),
]
