from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ChecklistListView.as_view(), name='list'),
    url(r'^list/$', views.checklist_filter_list, name='filter'),
    url(r'^(?P<pk>\d+)/$', views.ChecklistDetailView.as_view(), name='detail'),
    url(r'^create/$', views.ChecklistCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.ChecklistUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.ChecklistDeleteView.as_view(), name='delete'),
]
