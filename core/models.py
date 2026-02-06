import uuid
import os
from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization_id = models.ForeignKey("organizations.Organizations", on_delete=models.CASCADE, related_name="%(class)ss")
    branch_id = models.ForeignKey("organizations.Branch", on_delete=models.CASCADE, related_name="branch_%(class)ss")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

def employee_avatar_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]

    return (
        f"organizations/{instance.organization_id}/"
        f"employee/{instance.id or uuid.uuid4()}"
        f"/avatar{ext}"
    )

def student_avatar_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]

    return (
        f"organizations/{instance.organization_id}/"
        f"student/{instance.id or uuid.uuid4()}"
        f"/avatar{ext}"
    )


def exam_files_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]

    return (
        f"organizations/{instance.organization_id}/"
        f"exam/{instance.id or uuid.uuid4()}"
        f"/file{ext}"
    )

class Gender(models.TextChoices):
    MALE = "M", "Erkak"
    FEMALE = "F", "Ayol"
