# from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'academies'
urlpatterns = [
    #url(r'^academyupdate/$', views.UpdateStudent.as_view(), name='academyupdate'),
    url(r'^academyadd/$', views.AcademyView.as_view(), name='academyadd')
]