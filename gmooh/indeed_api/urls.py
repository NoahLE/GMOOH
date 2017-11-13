from django.conf.urls import url
from django.views.generic import TemplateView

from .views import index

app_name = 'indeed_api'
urlpatterns = [
    url(r'^$', index, name='index'),
]
