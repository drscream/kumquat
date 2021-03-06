from django.conf.urls import url
from cron import views

urlpatterns = [
	url(r'^job/$',                            views.CronjobList.as_view(),     name='cronjob_list'),
	url(r'^job/add$',                         views.CronjobCreate.as_view(),   name='cronjob_add'),
	url(r'^job/(?P<pk>\d+)/update$',          views.CronjobUpdate.as_view(),   name='cronjob_update'),
	url(r'^job/(?P<pk>\d+)/delete$',          views.CronjobDelete.as_view(),   name='cronjob_delete'),
]
