from django.urls import path, include
from rest_framework import routers

from author import urls
from author import views 

router = routers.DefaultRouter()
router.register(r'author', views.AuthorViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", include(router.urls))
]
