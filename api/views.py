from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Project, Task, Incident, Sprint, Comment
from .serializers import (
    UserSerializer, ProjectSerializer, TaskSerializer,
    IncidentSerializer, SprintSerializer, CommentSerializer
)
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Permite el registro (acción 'create') a cualquier usuario.
        Para las demás acciones, requiere autenticación.
        """
        if self.action == 'create':
            return [AllowAny()]
        # return [IsAuthenticated()]
        return [AllowAny()]
@api_view(['GET'])
@permission_classes([AllowAny])
def dashboard_stats(request):
    incidencias_count = Incident.objects.count()
    proyectos_count = Project.objects.count()
    tareas_count = Task.objects.count()

    data = {
        "incidencias": incidencias_count,
        "proyectos": proyectos_count,
        "tareas": tareas_count,
    }
    return Response(data)
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]  # 👈 acceso libre para pruebas


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny] 

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [AllowAny] 


class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = [AllowAny] 


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
