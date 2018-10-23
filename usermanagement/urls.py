from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from . import views

app_name='usermanagement'
urlpatterns = [
    # API
    # url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^authtoken', obtain_jwt_token),
    url(r'^logout$', views.LogoutView.as_view(), name='logout')
]
