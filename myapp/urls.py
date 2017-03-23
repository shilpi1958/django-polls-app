
from django.conf.urls import url,patterns
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from myapp import views

"""urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]"""
urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)


