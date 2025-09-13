import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# ---------- User ----------
class User(AbstractUser):
    ROLES = [
        ("Admin", "Admin"),
        ("PM", "Project Manager"),
        ("Member", "Member"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLES, default="Member")

# ---------- Project ----------
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name="owned_projects", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)

# ---------- Sprint ----------
class Sprint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    goal = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name="sprints", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

# ---------- Task ----------
class Task(models.Model):
    STATUS = [
        ("Pending", "Pending"),
        ("InProgress", "In Progress"),
        ("InReview", "In Review"),
        ("Done", "Done"),
    ]
    PRIORITY = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    priority = models.CharField(max_length=20, choices=PRIORITY, default="Medium")
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    sprint = models.ForeignKey(Sprint, null=True, blank=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="subtasks", on_delete=models.CASCADE)
    dependencies = models.ManyToManyField("self", symmetrical=False, related_name="blocking", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# ---------- Incident ----------
class Incident(models.Model):
    STATUS = [
        ("Open", "Open"),
        ("Assigned", "Assigned"),
        ("Resolved", "Resolved"),
        ("Closed", "Closed"),
    ]
    PRIORITY = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default="Open")
    priority = models.CharField(max_length=20, choices=PRIORITY, default="Medium")
    project = models.ForeignKey(Project, related_name="incidents", on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, related_name="reported_incidents", on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_incidents")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# ---------- Comment ----------
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Relación genérica
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")
