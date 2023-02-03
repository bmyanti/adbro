from rest_framework import routers
from django.urls import path

from src.advertisement import views

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'^event/domain', views.ListEventViewSet)
router.register(r'^event', views.EventViewSet)

urlpatterns = router.urls
