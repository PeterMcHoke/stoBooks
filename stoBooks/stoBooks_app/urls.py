from django.conf.urls import url
from django.contrib import admin
from stoBooks_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.profile, name='user-profile'),
    url(r'^search/', views.search, name='search'),
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^admin/', admin.site.urls)
]
