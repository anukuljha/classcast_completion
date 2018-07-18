from django.conf.urls import url
import views


urlpatterns = [
    url(r'^completed/$', views.completed, name='completed'),
    url(r'^get_progress/$', views.get_progress, name='get_progress'),
		]
