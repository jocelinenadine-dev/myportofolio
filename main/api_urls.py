from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.api_views import ExperienceViewSet, AwardViewSet

router = DefaultRouter()
router.register(r'experiences', ExperienceViewSet, basename='api-experience')
router.register(r'awards', AwardViewSet, basename='api-award')

urlpatterns = [
    path('', include(router.urls)),
]
