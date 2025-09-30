from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ProjectViewSet, TaskViewSet,
    IncidentViewSet, SprintViewSet, CommentViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"login", UserViewSet, basename='login')
router.register(r"projects", ProjectViewSet, basename='projects')
router.register(r"tasks", TaskViewSet)
router.register(r"incidents", IncidentViewSet)
router.register(r"sprints", SprintViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/tasks/", TaskViewSet.as_view({"get": "list"})),

    
]
