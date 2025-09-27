from rest_framework import serializers
from .models import User, Project, Task, Incident, Sprint, Comment

class UserSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source="first_name", required=True)
    apellido = serializers.CharField(source="last_name", required=True)
    correo = serializers.EmailField(source="email", required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "nombre", "apellido", "correo", "role"]
        extra_kwargs = {
            "password": {"write_only": True},  # nunca devolver la contraseña
            "role": {"required": False, "default": "Member"}  # opcional
        }

    def create(self, validated_data):
        # Mapear campos con 'source'
        first_name = validated_data.pop("first_name", "")
        last_name = validated_data.pop("last_name", "")
        email = validated_data.pop("email", "")
        password = validated_data.pop("password", "")
        role = validated_data.pop("role", "Member")

        # Crear usuario usando create_user para encriptar la contraseña
        user = User.objects.create_user(
            username=validated_data["username"],
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        user.role = role
        user.save()
        return user

# Serializers para otras entidades
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
