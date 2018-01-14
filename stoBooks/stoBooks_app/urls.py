from django.conf.urls import url
from django.contrib import admin
from stoBooks_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user-profile', views.profile, name='user-profile'),
    url(r'^search/', views.search, name='search'),
    url(r'^buy/', views.buy, name='buy'),
    url(r'^sell/', views.sell, name='sell'),
    url(r'^admin/', admin.site.urls)
]
