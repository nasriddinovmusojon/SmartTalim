from django.test import TestCase
from django.contrib.auth.models import Permission
from accounts.models import User, Employee, Role, RolePermission, UserRole
from organizations.models import Organizations, Branch
from accounts.serializers import (
    UserSerializer,
    EmployeeSerializer,
    RoleSerializer,
    RolePermissionSerializer,
    UserRoleSerializer
)

class UserModelTests(TestCase):

    def test_create_user(self):
        organization = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(
            organization_id=organization,
            name="Main Branch"
        )

        user = User.objects.create_user(
            username="testuser",
            password="123456",
            email="ibrohimjon@gmail.com",
            phone="+998901234567",
            full_name="Test User",
            organization_id=organization,
            branch_id=branch
        )


class EmployeeModelTests(TestCase):

    def test_create_employee(self):
        organization = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(
            organization_id=organization,
            name="Main Branch"
        )

        user = User.objects.create_user(
            username="employee1",
            password="123456",
            email="ibrohimjon@gmail.com",
            phone="+998911234567",
            full_name="Employee User",
            organization_id=organization,
            branch_id=branch
        )

        employee = Employee.objects.create(
            user=user,
            position="Manager",
            organization_id=organization,
            branch_id=branch
        )


class RoleModelTests(TestCase):

    def test_create_role(self):
        organization = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(
            organization_id=organization,
            name="Main Branch"
        )

        role = Role.objects.create(
            name="Admin",
            organization_id=organization,
            branch_id=branch
        )


class RolePermissionModelTests(TestCase):

    def test_create_role_permission(self):
        organization = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(
            organization_id=organization,
            name="Main Branch"
        )

        role = Role.objects.create(
            name="Ibrohimjon",
            organization_id=organization,
            branch_id=branch
        )

        permission = Permission.objects.first()


        role_permission = RolePermission.objects.create(
            role=role,
            permission=permission
        )


class UserRoleModelTests(TestCase):

    def test_create_user_role(self):
        organization = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(
            organization_id=organization,
            name="Main Branch"
        )

        user = User.objects.create_user(
            username="roleuser",
            password="123456",
            email="ibrohimjon@gmail.com",
            phone="+998931234567",
            full_name="Role User",
            organization_id=organization,
            branch_id=branch
        )

        role = Role.objects.create(
            name="Teacher",
            organization_id=organization,
            branch_id=branch
        )

        user_role = UserRole.objects.create(
            user=user,
            role=role
        )




class SerializerTests(TestCase):

    def test_all_serializers(self):

        organization = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(
            organization_id=organization,
            name="Main Branch"
        )


        user_data = {
            "username": "testuser",
            "password": "123456",
            "email": "test@gmail.com",
            "phone": "+998901234567",
            "full_name": "Test User",
            "organization_id": organization.id,
            "branch_id": branch.id
        }
        user_serializer = UserSerializer(data=user_data)
        self.assertTrue(user_serializer.is_valid())
        user = user_serializer.save()


        employee_data = {
            "user": user.id,
            "position": "Manager",
            "organization_id": organization.id,
            "branch_id": branch.id
        }
        employee_serializer = EmployeeSerializer(data=employee_data)
        self.assertTrue(employee_serializer.is_valid())
        employee = employee_serializer.save()

        role_data = {
            "name": "Admin",
            "organization_id": organization.id,
            "branch_id": branch.id
        }
        role_serializer = RoleSerializer(data=role_data)
        self.assertTrue(role_serializer.is_valid())
        role = role_serializer.save()


        permission = Permission.objects.first()
        role_permission_data = {
            "role": role.id,
            "permission": permission.id
        }
        role_permission_serializer = RolePermissionSerializer(data=role_permission_data)
        self.assertTrue(role_permission_serializer.is_valid())
        role_permission = role_permission_serializer.save()


        user_role_data = {
            "user": user.id,
            "role": role.id
        }
        user_role_serializer = UserRoleSerializer(data=user_role_data)
        self.assertTrue(user_role_serializer.is_valid())
        user_role = user_role_serializer.save()


        self.assertEqual(employee.user, user)
        self.assertEqual(role_permission.role, role)
        self.assertEqual(user_role.user, user)

