from django.conf.urls import url
from music import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.record_detail, name='record_detail'),
    url(r'^add/$', views.RecordCreate.as_view(), name='add-record'),
    url(r'^(?P<pk>[0-9]+)/update/', views.RecordUpdate.as_view(), name='update-record'),
    # url(r'^record/(?P<pk>[0-9]+)/delete/', views.RecordDelete.as_view(), name='delete-record'),
]
