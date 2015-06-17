from django.conf.urls import include, url
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', 'food.views.index_page', name='index'),
    url(r'^vote/(?P<restaurant_id>\d+)$', 'food.views.vote', name='vote'),
    url(r'^login/?$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/?$', views.logout, name='logout')
]
