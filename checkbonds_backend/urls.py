from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^usermanagement/', include('usermanagement.urls')),
    url(r'^da-control/', admin.site.urls),

]
