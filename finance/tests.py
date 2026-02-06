from django.test import TestCase
from django.utils import timezone
from finance.models import ExpenseCategory, Expenses
from organizations.models import Organizations, Branch
from .serializers import ExpenseCategorySerializer, ExpensesSerializer

class ExpenseCategoryTest(TestCase):
    def test_expense_category_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")

        ExpenseCategory.objects.create(
            name="Office",
            branch_id=branch,        # majburiy
            organization_id=org      # majburiy
        )

class ExpensesTest(TestCase):
    def test_expense_create(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(organization_id=org, name="Main Branch")

        category = ExpenseCategory.objects.create(
            name="Internet",
            branch_id=branch,
            organization_id=org
        )

        Expenses.objects.create(
            category=category,
            amount=150000,
            expense_date=timezone.now(),
            comment="Oylik internet to‘lovi",
            branch_id=branch,        # majburiy
            organization_id=org      # majburiy
        )



class ExpenseCategorySerializerTest(TestCase):
    def test_expense_category_serializer(self):
        serializer = ExpenseCategorySerializer

class ExpensesSerializerTest(TestCase):
    def test_expenses_serializer(self):
        serializer = ExpensesSerializer