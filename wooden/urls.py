"""wooden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from woodenapi.views.auth import login_user, register_user
from woodenapi.views.builder import BuilderView
from woodenapi.views.category import CategoryView
from woodenapi.views.lumber import LumberView
from woodenapi.views.project import ProjectView
from woodenapi.views.tag import TagView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'builders', BuilderView, 'builder')
router.register(r'categories', CategoryView, 'category')
router.register(r'lumber', LumberView, 'lumber')
router.register(r'tags', TagView, 'tag')
router.register(r'projects', ProjectView, 'project')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls))
]
