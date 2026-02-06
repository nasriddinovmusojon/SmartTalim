from django.test import TestCase
from uuid import uuid4
from django.utils import timezone
from .models import SmsTemplates, SmsSchedules, SMSMessages
from accounts.models import User, Employee
from organizations.models import Organizations, Branch
from .serializers import SmsTemplatesSerializer, SmsSchedulesSerializer, SMSMessagesSerializer

class SmsTemplatesTest(TestCase):
    def test_sms_template_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")

        user = User.objects.create_user(
            username="smsuser",
            password="123456",
            email="ibrohimjon@gmail.com",
            phone="+998900000100",
            full_name="SMS User",
            organization_id=org,
            branch_id=branch
        )

        employee = Employee.objects.create(
            user=user,
            position="Admin",
            organization_id=org,
            branch_id=branch
        )

        SmsTemplates.objects.create(
            name="Test Template",
            text="Salom, bu test SMS",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )


class SmsSchedulesTest(TestCase):
    def test_sms_schedule_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")

        user = User.objects.create_user(
            username="scheduleuser",
            password="123456",
            email="scheduleuser@gmail.com",
            phone="+998901401223",
            full_name="Schedule User",
            organization_id=org,
            branch_id=branch
        )

        employee = Employee.objects.create(
            user=user,
            position="Manager",
            organization_id=org,
            branch_id=branch
        )

        template = SmsTemplates.objects.create(
            name="Schedule Template",
            text="Rejali SMS",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )

        SmsSchedules.objects.create(
            name="Test Schedule",
            target_type="student",
            target_id=uuid4(),
            template=template,
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )


class SmsSchedulesDuplicateTest(TestCase):
    def test_sms_schedule_create_duplicate(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")

        user = User.objects.create_user(
            username="scheduleuser2",
            password="123456",
            email="scheduleuser2@gmail.com",
            phone="+998900000101",
            full_name="Schedule User 2",
            organization_id=org,
            branch_id=branch
        )

        employee = Employee.objects.create(
            user=user,
            position="Manager",
            organization_id=org,
            branch_id=branch
        )

        template = SmsTemplates.objects.create(
            name="Schedule Template 2",
            text="Rejali SMS 2",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )

        SmsSchedules.objects.create(
            name="Test Schedule 2",
            target_type="student",
            target_id=uuid4(),
            template=template,
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )


class SMSMessagesTest(TestCase):
    def test_sms_message_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")

        user = User.objects.create_user(
            username="messageuser",
            password="123456",
            email="messageuser@gmail.com",
            phone="+998900000102",
            full_name="Message User",
            organization_id=org,
            branch_id=branch
        )

        employee = Employee.objects.create(
            user=user,
            position="Operator",
            organization_id=org,
            branch_id=branch
        )

        template = SmsTemplates.objects.create(
            name="Message Template",
            text="Oddiy SMS",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )

        schedule = SmsSchedules.objects.create(
            name="Message Schedule",
            target_type="lead",
            target_id=uuid4(),
            template=template,
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )


        SMSMessages.objects.create(
            recipent_type="student",
            recipent_id=uuid4(),
            phone="+998901234567",
            text="Salom test",
            template=template,
            schedule=schedule,
            send_type="manual",
            status="pending",
            sent_at=timezone.now(),
            branch_id=branch,
            organization_id=org
        )




class SmsTemplatesSerializerTest(TestCase):
    def test_serializer(self):
        serializer = SmsTemplatesSerializer

class SmsSchedulesSerializerTest(TestCase):
    def test_serializer(self):
        serializer = SmsSchedulesSerializer

class SMSMessagesSerializerTest(TestCase):
    def test_serializer(self):
        serializer = SMSMessagesSerializer