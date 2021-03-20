"""fp_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from fpApi.views.menuItem import MenuItemViewSet
from fpApi.views.restaurants import RestaurantViewSet
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from fpApi.models import *
from fpApi.views import *
from django.urls import path

# pylint: disable=invalid-name
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UsersViewset, 'user')
router.register(r'restaurants', RestaurantViewSet, 'restaurant')
router.register(r'menuitems', MenuItemViewSet, 'menuitem')
router.register(r'reviews', ReviewViewSet, 'review')

urlpatterns = [
    # url(r'^reviews$', include('review-list')),
    url(r'^', include(router.urls)),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
    url(r'^api-token-auth$', obtain_auth_token),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
