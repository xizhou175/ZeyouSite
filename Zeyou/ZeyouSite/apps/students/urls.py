# from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'students'
urlpatterns = [
    url(r'^studentupdate/$', views.UpdateStudent.as_view(), name='studentupdate'),
    url(r'^studentadd/$', views.StudentView.as_view(), name='studentadd')
]