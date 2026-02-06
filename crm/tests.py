from django.test import TestCase
from uuid import uuid4
from crm.models import (
    CRMSource, CRMPipelines, CRMLead,
    CRMActivity, CRMLeadsHistory,
    CRMLostReason, CRMLeadLost, CRMLeadNotes
)
from accounts.models import User
from organizations.models import Organizations, Branch
from .serializers import (
    CRMSourceSerializer, CRMPipelinesSerializer, CRMLeadSerializer,
    CRMActivitySerializer, CRMLeadsHistorySerializer, CRMLostReasonSerializer,
    CRMLeadLostSerializer, CRMLeadNotesSerializer
)


class CRMSourceTest(TestCase):
    def test_source_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")
        CRMSource.objects.create(
            name="Instagram",
            branch_id=branch,
            organization_id=org
        )


class CRMLeadTest(TestCase):
    def test_lead_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")
        source = CRMSource.objects.create(name="Website", branch_id=branch, organization_id=org)
        pipeline = CRMPipelines.objects.create(name="Initial", position=1, branch_id=branch, organization_id=org)
        user = User.objects.create_user(
            username="crmuser",
            password="123456",
            email="crmuser@gmail.com",
            phone="+998900001000",
            full_name="CRM User",
            organization_id=org,
            branch_id=branch
        )
        CRMLead.objects.create(
            full_name="Ali Valiyev",
            phone_number="+998901234567",
            source=source,
            pipline=pipeline,
            assigned_to=user,
            converted_student_id=1,
            branch_id=branch,
            organization_id=org
        )


class CRMActivityTest(TestCase):
    def test_activity_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")
        source = CRMSource.objects.create(name="Telegram", branch_id=branch, organization_id=org)
        pipeline = CRMPipelines.objects.create(name="Contacted", position=2, branch_id=branch, organization_id=org)
        user = User.objects.create_user(
            username="activityuser",
            password="123456",
            email="activityuser@gmail.com",
            phone="+998900001001",
            full_name="Activity User",
            organization_id=org,
            branch_id=branch
        )
        lead = CRMLead.objects.create(
            full_name="Test Lead",
            phone_number="+998901234568",
            source=source,
            pipline=pipeline,
            assigned_to=user,
            converted_student_id=2,
            branch_id=branch,
            organization_id=org
        )
        CRMActivity.objects.create(
            lead=lead,
            activity_type="call",
            created_by=user,
            branch_id=branch,
            organization_id=org
        )


class CRMLeadsHistoryTest(TestCase):
    def test_lead_history_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")
        source = CRMSource.objects.create(name="Ad", branch_id=branch, organization_id=org)
        pipeline1 = CRMPipelines.objects.create(name="New", position=1, branch_id=branch, organization_id=org)
        pipeline2 = CRMPipelines.objects.create(name="In Progress", position=2, branch_id=branch, organization_id=org)
        user = User.objects.create_user(
            username="historyuser",
            password="123456",
            email="historyuser@gmail.com",
            phone="+998900001002",
            full_name="History User",
            organization_id=org,
            branch_id=branch
        )
        lead = CRMLead.objects.create(
            full_name="History Lead",
            phone_number="+998901234569",
            source=source,
            pipline=pipeline1,
            assigned_to=user,
            converted_student_id=3,
            branch_id=branch,
            organization_id=org
        )
        CRMLeadsHistory.objects.create(
            lead=lead,
            old_pipeline=pipeline1,
            new_pipeline=pipeline2,
            changed_by=user,
            branch_id=branch,
            organization_id=org
        )


class CRMLostReasonTest(TestCase):
    def test_lost_reason_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")
        CRMLostReason.objects.create(
            name="No interest",
            branch_id=branch,
            organization_id=org
        )


class CRMLeadLostTest(TestCase):
    def test_lead_lost_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")
        source = CRMSource.objects.create(name="Call", branch_id=branch, organization_id=org)
        pipeline = CRMPipelines.objects.create(name="Lost", position=3, branch_id=branch, organization_id=org)
        reason = CRMLostReason.objects.create(name="Expensive", branch_id=branch, organization_id=org)
        user = User.objects.create_user(
            username="lostuser",
            password="123456",
            email="lostuser@gmail.com",
            phone="+998900001003",
            full_name="Lost User",
            organization_id=org,
            branch_id=branch
        )
        lead = CRMLead.objects.create(
            full_name="Lost Lead",
            phone_number="+998901234570",
            source=source,
            pipline=pipeline,
            assigned_to=user,
            converted_student_id=4,
            branch_id=branch,
            organization_id=org
        )
        CRMLeadLost.objects.create(
            lead=lead,
            reason=reason,
            comment="Narxi qimmat",
            branch_id=branch,
            organization_id=org
        )


class CRMLeadNotesTest(TestCase):
    def test_lead_note_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")
        source = CRMSource.objects.create(name="Referral", branch_id=branch, organization_id=org)
        pipeline = CRMPipelines.objects.create(name="Note", position=4, branch_id=branch, organization_id=org)
        user = User.objects.create_user(
            username="noteuser",
            password="123456",
            email="noteuser@gmail.com",
            phone="+998900001004",
            full_name="Note User",
            organization_id=org,
            branch_id=branch
        )
        lead = CRMLead.objects.create(
            full_name="Note Lead",
            phone_number="+998901234571",
            source=source,
            pipline=pipeline,
            assigned_to=user,
            converted_student_id=5,
            branch_id=branch,
            organization_id=org
        )
        CRMLeadNotes.objects.create(
            lead=lead,
            user=user,
            note="Bu lead bilan yana bog‘lanish kerak",
            branch_id=branch,
            organization_id=org
        )




class CRMSourceSerializerTest(TestCase):
    def test_crm_source_serializer(self):
        serializer = CRMSourceSerializer

class CRMPipelinesSerializerTest(TestCase):
    def test_crm_pipelines_serializer(self):
        serializer = CRMPipelinesSerializer

class CRMLeadSerializerTest(TestCase):
    def test_crm_lead_serializer(self):
        serializer = CRMLeadSerializer

class CRMActivitySerializerTest(TestCase):
    def test_crm_activity_serializer(self):
        serializer = CRMActivitySerializer

class CRMLeadsHistorySerializerTest(TestCase):
    def test_crm_leads_history_serializer(self):
        serializer = CRMLeadsHistorySerializer

class CRMLostReasonSerializerTest(TestCase):
    def test_crm_lost_reason_serializer(self):
        serializer = CRMLostReasonSerializer

class CRMLeadLostSerializerTest(TestCase):
    def test_crm_lead_lost_serializer(self):
        serializer = CRMLeadLostSerializer

class CRMLeadNotesSerializerTest(TestCase):
    def test_crm_lead_notes_serializer(self):
        serializer = CRMLeadNotesSerializer