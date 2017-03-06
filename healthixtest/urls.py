from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.index, name = 'index'), url(r'^view_tests/$', views.view_tests, name = 'view_tests'), url(r'^view_tests/$', views.view_tests, name='view_tests'),
]
