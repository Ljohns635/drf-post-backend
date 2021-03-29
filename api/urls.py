from django.conf.urls import include, url
from rest_framework import routers

from api.views import GhostPostViewSet

router = routers.DefaultRouter()

router.register(r'ghostpost', GhostPostViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
