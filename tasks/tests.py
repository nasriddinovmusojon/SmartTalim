from django.test import TestCase
from django.utils import timezone
from tasks.models import (
    TaskBoards, TaskColumns, Task,
    TaskComments, TaskActivityLogs,
    TaskNotifications, TaskPermissions
)
from accounts.models import User, Employee
from organizations.models import Organizations, Branch
from tasks.serializers import (
    TaskBoardsSerializer, TaskColumnsSerializer, TaskSerializer,
    TaskCommentsSerializer, TaskActivityLogsSerializer,
    TaskNotificationsSerializer, TaskPermissionsSerializer
)

class TaskBoardsTest(TestCase):
    def test_task_board_create(self):
        org = Organizations.objects.create(
            name="Test Org",
            address="Test address",
            phone="+998900000000",
            status="active"
        )
        branch = Branch.objects.create(
            organization_id=org,
            name="Main Branch",
            address="Branch address",
            phone="+998900000001"
        )
        user = User.objects.create_user(
            username="boarduser",
            password="123456",
            email="boarduser@test.com",
            phone="+998900002000",
            full_name="Board User",
            organization_id=org,
            branch_id=branch
        )
        employee = Employee.objects.create(
            user=user,
            position="Admin",
            organization_id=org,
            branch_id=branch
        )
        TaskBoards.objects.create(
            name="Test Board",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )

class TaskColumnsTest(TestCase):
    def test_task_column_create(self):
        org = Organizations.objects.create(
            name="Test Org",
            address="Test address",
            phone="+998900000002",
            status="active"
        )
        branch = Branch.objects.create(
            organization_id=org,
            name="Main Branch",
            address="Branch address",
            phone="+998900000003"
        )
        user = User.objects.create_user(
            username="columnuser",
            password="123456",
            email="columnuser@test.com",
            phone="+998900002001",
            full_name="Column User",
            organization_id=org,
            branch_id=branch
        )
        employee = Employee.objects.create(
            user=user,
            position="Admin",
            organization_id=org,
            branch_id=branch
        )
        board = TaskBoards.objects.create(
            name="Board",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )
        TaskColumns.objects.create(
            board=board,
            name="To Do",
            position=1,
            branch_id=branch,
            organization_id=org
        )

class TaskTest(TestCase):
    def test_task_create(self):
        org = Organizations.objects.create(
            name="Test Org",
            address="Test address",
            phone="+998900000004",
            status="active"
        )
        branch = Branch.objects.create(
            organization_id=org,
            name="Main Branch",
            address="Branch address",
            phone="+998900000005"
        )
        user = User.objects.create_user(
            username="taskuser",
            password="123456",
            email="taskuser@test.com",
            phone="+998900002002",
            full_name="Task User",
            organization_id=org,
            branch_id=branch
        )
        employee = Employee.objects.create(
            user=user,
            position="Manager",
            organization_id=org,
            branch_id=branch
        )
        board = TaskBoards.objects.create(
            name="Main Board",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )
        column = TaskColumns.objects.create(
            board=board,
            name="In Progress",
            position=2,
            branch_id=branch,
            organization_id=org
        )
        Task.objects.create(
            board=board,
            column=column,
            title="Test Task",
            description="Oddiy task",
            assigned_to=employee,
            created_by=employee,
            deadline=timezone.now(),
            priority="medium",
            status="active",
            branch_id=branch,
            organization_id=org
        )

class TaskCommentsTest(TestCase):
    def test_task_comment_create(self):
        org = Organizations.objects.create(
            name="Test Org",
            address="Test address",
            phone="+998900000006",
            status="active"
        )
        branch = Branch.objects.create(
            organization_id=org,
            name="Main Branch",
            address="Branch address",
            phone="+998900000007"
        )
        user = User.objects.create_user(
            username="commentuser",
            password="123456",
            email="commentuser@test.com",
            phone="+998900002003",
            full_name="Comment User",
            organization_id=org,
            branch_id=branch
        )
        employee = Employee.objects.create(
            user=user,
            position="Developer",
            organization_id=org,
            branch_id=branch
        )
        board = TaskBoards.objects.create(
            name="Board",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )
        column = TaskColumns.objects.create(
            board=board,
            name="Done",
            position=3,
            branch_id=branch,
            organization_id=org
        )
        task = Task.objects.create(
            board=board,
            column=column,
            title="Comment Task",
            description="Task desc",
            assigned_to=employee,
            created_by=employee,
            deadline=timezone.now(),
            priority="low",
            status="active",
            branch_id=branch,
            organization_id=org
        )
        TaskComments.objects.create(
            task=task,
            user=employee,
            comment="Bu comment",
            branch_id=branch,
            organization_id=org
        )

class TaskActivityLogsTest(TestCase):
    def test_task_activity_log_create(self):
        org = Organizations.objects.create(
            name="Test Org",
            address="Test address",
            phone="+998900000008",
            status="active"
        )
        branch = Branch.objects.create(
            organization_id=org,
            name="Main Branch",
            address="Branch address",
            phone="+998900000009"
        )
        user = User.objects.create_user(
            username="loguser",
            password="123456",
            email="loguser@test.com",
            phone="+998900002004",
            full_name="Log User",
            organization_id=org,
            branch_id=branch
        )
        employee = Employee.objects.create(
            user=user,
            position="Admin",
            organization_id=org,
            branch_id=branch
        )
        board = TaskBoards.objects.create(
            name="Board",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )
        column = TaskColumns.objects.create(
            board=board,
            name="To Do",
            position=1,
            branch_id=branch,
            organization_id=org
        )
        task = Task.objects.create(
            board=board,
            column=column,
            title="Log Task",
            description="Log desc",
            assigned_to=employee,
            created_by=employee,
            deadline=timezone.now(),
            priority="high",
            status="active",
            branch_id=branch,
            organization_id=org
        )
        TaskActivityLogs.objects.create(
            task=task,
            user=employee,
            branch_id=branch,
            organization_id=org
        )

class TaskNotificationsTest(TestCase):
    def test_task_notification_create(self):
        org = Organizations.objects.create(
            name="Test Org",
            address="Test address",
            phone="+998900000010",
            status="active"
        )
        branch = Branch.objects.create(
            organization_id=org,
            name="Main Branch",
            address="Branch address",
            phone="+998900000011"
        )
        user = User.objects.create_user(
            username="notifyuser",
            password="123456",
            email="notifyuser@test.com",
            phone="+998900002005",
            full_name="Notify User",
            organization_id=org,
            branch_id=branch
        )
        employee = Employee.objects.create(
            user=user,
            position="Staff",
            organization_id=org,
            branch_id=branch
        )
        board = TaskBoards.objects.create(
            name="Board",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )
        column = TaskColumns.objects.create(
            board=board,
            name="Review",
            position=4,
            branch_id=branch,
            organization_id=org
        )
        task = Task.objects.create(
            board=board,
            column=column,
            title="Notify Task",
            description="Notify desc",
            assigned_to=employee,
            created_by=employee,
            deadline=timezone.now(),
            priority="urgent",
            status="active",
            branch_id=branch,
            organization_id=org
        )
        TaskNotifications.objects.create(
            task=task,
            user=employee,
            notify_at=timezone.now(),
            branch_id=branch,
            organization_id=org
        )

class TaskPermissionsTest(TestCase):
    def test_task_permission_create(self):
        org = Organizations.objects.create(
            name="Test Org",
            address="Test address",
            phone="+998900000012",
            status="active"
        )
        branch = Branch.objects.create(
            organization_id=org,
            name="Main Branch",
            address="Branch address",
            phone="+998900000013"
        )
        user = User.objects.create_user(
            username="permuser",
            password="123456",
            email="permuser@test.com",
            phone="+998900002006",
            full_name="Perm User",
            organization_id=org,
            branch_id=branch
        )
        employee = Employee.objects.create(
            user=user,
            position="Staff",
            organization_id=org,
            branch_id=branch
        )
        board = TaskBoards.objects.create(
            name="Board",
            created_by=employee,
            branch_id=branch,
            organization_id=org
        )
        column = TaskColumns.objects.create(
            board=board,
            name="Permissions",
            position=5,
            branch_id=branch,
            organization_id=org
        )
        task = Task.objects.create(
            board=board,
            column=column,
            title="Permission Task",
            description="Permission desc",
            assigned_to=employee,
            created_by=employee,
            deadline=timezone.now(),
            priority="medium",
            status="active",
            branch_id=branch,
            organization_id=org
        )
        TaskPermissions.objects.create(
            task=task,
            user=employee,
            branch_id=branch,
            organization_id=org
        )




class TaskBoardsSerializerTest(TestCase):
    def test_task_boards_serializer(self):
        serializer = TaskBoardsSerializer

class TaskColumnsSerializerTest(TestCase):
    def test_task_columns_serializer(self):
        serializer = TaskColumnsSerializer

class TaskSerializerTest(TestCase):
    def test_task_serializer(self):
        serializer = TaskSerializer

class TaskCommentsSerializerTest(TestCase):
    def test_task_comments_serializer(self):
        serializer = TaskCommentsSerializer

class TaskActivityLogsSerializerTest(TestCase):
    def test_task_activity_logs_serializer(self):
        serializer = TaskActivityLogsSerializer

class TaskNotificationsSerializerTest(TestCase):
    def test_task_notifications_serializer(self):
        serializer = TaskNotificationsSerializer

class TaskPermissionsSerializerTest(TestCase):
    def test_task_permissions_serializer(self):
        serializer = TaskPermissionsSerializer