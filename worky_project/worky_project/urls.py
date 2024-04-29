"""
URL configuration for worky_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from worky.views import *
from rest_framework import routers


# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={"suffix": 'list'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={"suffix": 'Detail'})
#     ]
#
#
# router = MyCustomRouter()
# router.register(r'clients', ClientViewSet, basename="clients")
# print(router.urls)

# router = routers.SimpleRouter()
# router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('worky/', include('worky.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/clients/', ClientAPIList.as_view()),
    path('api/v1/clients/<int:pk>/', ClientAPIUpdate.as_view()),
    path('api/v1/clientsdelete/<int:pk>/', ClientAPIDestroyView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/', include(router.urls))
    # path('api/v1/clientlist/', ClientViewSet.as_view({"get": "list"})),
    # path('api/v1/clientlist/<int:pk>/', ClientViewSet.as_view({"put": "update"})),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
