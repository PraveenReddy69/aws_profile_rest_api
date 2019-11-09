from django.urls import path, include

from profiles_api import views
from .views import HelloViewSet
from .views import UserProfileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile',UserProfileViewSet)


urlpatterns=[
    path('hello_view/', views.HelloAPIview.as_view()),
    path('', include(router.urls))
]
