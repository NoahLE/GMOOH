from django.conf.urls import url
from django.views.generic import TemplateView

from .views import index, search, results, hide_listing, update_listings

app_name = 'indeed_api'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^search/$', search, name='search'),
    url(r'^results/$', results, name='results'),
    url(r'^hide/(?P<listing_pk>[0-9a-f-]+)/$', hide_listing, name='hide_listing'),
    url(r'^update/(?P<listing_pk>[0-9a-f-]+)/$', update_listings, name='update_listing')
]
