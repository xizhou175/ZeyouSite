# from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^createuser/$', views.UserView.as_view(), name='createUser'),
    url(r'^authorizations/$', obtain_jwt_token, name='authorization'),
    url(r'^userupdate/$', views.UserUpdateView.as_view(), name='userUpdate'),
    url(r'^pwdupdate/$', views.UpdatePwdView.as_view(), name='pwdUpdate'),
    url(r'^upload/$', views.UploadView.as_view(), name='upload'),
    url(r'^parseexcel/$', views.ParseExcelView.as_view(), name='parseexcel'),
    url(r'^filterdepartment/$', views.FilterDepartmentView.as_view(), name='filterDepartment'),
    url(r'^personalinfo/$', views.PersonalInfoView.as_view(), name='personalInfo'),
    url(r'^lookupuser/$', views.LookupUser.as_view(), name='userLookup'),
    url(r'^deleteuser/$', views.DeleteUser.as_view(), name='userdelete')
]
