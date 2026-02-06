from django.test import TestCase
from uuid import uuid4
from audit.models import AuditLog, AuditEntityType, AuditAction
from accounts.models import User, Employee
from organizations.models import Organizations, Branch
from audit.serializers import AuditLogSerializer


class AuditLogTest(TestCase):

    def test_audit_log_create(self):

        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(
            organization_id=org,
            name="Main Branch"
        )


        user = User.objects.create_user(
            username="audituser",
            password="123456",
            email="audituser@gmail.com",
            phone="+998900000010",
            full_name="Audit User",
            organization_id=org,
            branch_id=branch
        )


        employee = Employee.objects.create(
            user=user,
            position="Admin",
            organization_id=org,
            branch_id=branch
        )


        AuditLog.objects.create(
            entity_type=AuditEntityType.USER,
            entity_id=uuid4(),
            action=AuditAction.CREATE,
            old_data=None,
            new_action={"username": "audituser"},
            performed_by=employee,
            performed_by_role="Admin",
            branch_id=branch,
            organization_id=org
        )


class AuditLogSerializerTest(TestCase):
    def test_audit_log_serializer(self):
        serializer = AuditLogSerializer


