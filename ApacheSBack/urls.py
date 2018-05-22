"""ApacheSBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include


from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from ApacheS import views
from ApacheSBack.v1.router import api_urlpatterns as api_v1

schema_view = get_schema_view(title='ApacheS API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='ApacheS API', description='RESTful API for ApacheS')),
    url(r'^schema/$', schema_view),

    url(r'^/v1/', include(api_v1)),

    url(r'^/v1/auth/obtain_token/', obtain_jwt_token),
    url(r'^/v1/auth/refresh_token/', refresh_jwt_token),
]