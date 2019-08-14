"""restserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
# from rest_framework.authtoken import obtain_auth_token
from backend.viewsets import (
    UserViewSet,
    ProfileViewSet,
    InquiryViewSet,
    RechargeViewSet,
    PrepaidViewSet,
    DongleViewSet,
    FeedbackViewSet,
    PreformViewSet,
    PostformViewSet,
    DongleformViewSet,
    CustomAuthToken,
)



user = routers.DefaultRouter()
user.register('login',UserViewSet)
# profile = routers.DefaultRouter()
user.register('profile',ProfileViewSet)
user.register('recharge',RechargeViewSet)
user.register('dongleplans',DongleViewSet)
user.register('plans',PrepaidViewSet)
user.register('inquiry',InquiryViewSet)
user.register('feedback',FeedbackViewSet)
user.register('form1',PreformViewSet)
user.register('form2',PostformViewSet)
user.register('form3',DongleformViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(user.urls)),
    path('auth/',CustomAuthToken.as_view(),name='auth')
]
