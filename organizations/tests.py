from django.test import TestCase
from uuid import uuid4
from .models import Organizations, Subscriptions, Branch
from django.utils import timezone
from .serializers import OrganizationsSerializer, SubscriptionsSerializer, BranchSerializer

class OrganizationsTest(TestCase):
    def test_organization_create(self):
        org = Organizations.objects.create(
            name="Test Org",
            logo=None,
            address="Toshkent, Uzbekistan",
            phone="+998901234567",
            status="active"
        )



class SubscriptionsTest(TestCase):
    def test_subscription_create(self):
        org = Organizations.objects.create(
            name="Sub Org",
            logo=None,
            address="Toshkent, Uzbekistan",
            phone="+998901234568",
            status="active"
        )
        sub = Subscriptions.objects.create(
            organization_id=org,
            plan_type="Premium",
            start_date=timezone.now(),
            end_date=timezone.now(),
            status="active",
            price=100000
        )



class BranchTest(TestCase):
    def test_branch_create(self):
        org = Organizations.objects.create(
            name="Branch Org",
            logo=None,
            address="Toshkent, Uzbekistan",
            phone="+998901234569",
            status="active"
        )
        branch = Branch.objects.create(
            organization_id=org,
            name="Main Branch",
            address="Toshkent, Yunusobod",
            phone="+998901234570",
            is_active=True
        )




class OrganizationsSerializerTest(TestCase):
    def test_organizations_serializer(self):
        serializer = OrganizationsSerializer

class SubscriptionsSerializerTest(TestCase):
    def test_subscriptions_serializer(self):
        serializer = SubscriptionsSerializer

class BranchSerializerTest(TestCase):
    def test_branch_serializer(self):
        serializer = BranchSerializer