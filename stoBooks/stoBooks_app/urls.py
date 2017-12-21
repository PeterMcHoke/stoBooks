from django.conf.urls import url
from django.contrib import admin
from stoBooks_app import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^user-profile/$', views.ProfilePageView.as_view()),
    url(r'^$', views.HomePageView.as_view()),
    url(r'^admin/', admin.site.urls)
]
