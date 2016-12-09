from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.upload_file, name='upload'),
    url(r'^results/$', views.results, name='results'),
	]