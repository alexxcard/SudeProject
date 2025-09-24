from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ProjectViewSet, TaskViewSet,
    IncidentViewSet, SprintViewSet, CommentViewSet
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"projects", basename='projects', viewset=ProjectViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"incidents", IncidentViewSet)
router.register(r"sprints", SprintViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
