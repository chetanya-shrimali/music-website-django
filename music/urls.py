from django.conf.urls import url
from music import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<record_id>[0-9]+)/$', views.record_detail, name='record_detail')
]
