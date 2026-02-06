from django.test import TestCase
from datetime import date
from django.utils import timezone
from decimal import Decimal
from datetime import datetime
from accounts.models import User
from accounts.models import Employee
from organizations.models import Organizations, Branch
from academics.models import (Student, Group, StudentGroup,
                              StudentPricing, Course,StudentBalances,
                              StudentTarnsactions, LeaveReason,StudentGroupLeaves,
                              StudentFreezes,StudentBalanceHistory,Attendence)
from academics.serializers import (
    StudentSerializer, StudentGroupSerializer, StudentPricingSerializer,
    StudentBalancesSerializer, StudentTarnsactionsSerializer,
    LeaveReasonSerializer, StudentGroupLeavesSerializer,
    StudentFreezesSerializer, StudentBalanceHistorySerializer,
    AttendenceSerializer, RoomSerializer, CourseSerializer, GroupSerializer, GroupTeacherSerializer,
    LessonTimeSerializer, LessonScheduleSerializer, ExamsSerializer, ExamResultsSerializer,
    TeacherSalaryRulesSerializer, TeacherSalaryPaymentsSerializer
)

# Create your tests here.

def create_employee(organization, branch, username="employee"):
    user = User.objects.create(username=username)
    user.set_password("123456")
    user.save()
    return Employee.objects.create(
        organization_id=organization,
        branch_id=branch,
        user=user
    )

# -------------------------------
# Student Testlari
# -------------------------------
class StudentModelTests(TestCase):
    def test_create_student(self):
        org = Organizations.objects.create(name="Test Org")
        br = Branch.objects.create(organization_id=org, name="Main Branch")
        Student.objects.create(
            organization_id=org,
            branch_id=br,
            full_name="Ali Valiyev",
            phone_number="+998901234567",
            phone_number2="+998911234568",
            password="123456",
            parent_name="Hasan Valiyev",
            parent_phone="+998931234567",
            email="ali@example.com",
            telegram_username="ali_valiyev",
            address="Toshkent shahri"
        )

# -------------------------------
# StudentGroup Testlari
# -------------------------------
class StudentGroupModelTests(TestCase):
    def test_create_student_group(self):
        org = Organizations.objects.create(name="Test Org")
        br = Branch.objects.create(organization_id=org, name="Main")
        student = Student.objects.create(
            organization_id=org,
            branch_id=br,
            full_name="Ali Valiyev",
            phone_number="901234567",
            phone_number2="911234568",
            password="123456",
            address="Toshkent"
        )
        group = Group.objects.create(
            organization_id=org,
            branch_id=br,
            name="Python Backend",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 6, 1)
        )
        StudentGroup.objects.create(
            student=student,
            group=group,
            organization_id=org,
            branch_id=br,
            joined_at=date(2025, 1, 1),
            left_at=date(2025, 6, 1),
            end_date=date(2025, 6, 1)
        )

# -------------------------------
# StudentPricing Testlari
# -------------------------------
class StudentPricingModelTests(TestCase):
    def test_create_student_pricing(self):
        org = Organizations.objects.create(name="Test Org")
        br = Branch.objects.create(organization_id=org, name="Main")
        student = Student.objects.create(
            organization_id=org,
            branch_id=br,
            full_name="Ali Valiyev",
            phone_number="901234561",
            phone_number2="911234561",
            password="123456",
            address="Toshkent"
        )
        course = Course.objects.create(
            organization_id=org,
            branch_id=br,
            name="Python Backend",
            monthly_price=Decimal("100000"),
            lesson_month=6
        )
        employee = create_employee(org, br, username="employee_pricing")
        StudentPricing.objects.create(
            student=student,
            course=course,
            price_override=Decimal("750000"),
            reason="Chegirma berildi",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 6, 1),
            created_by=employee,
            organization_id=org,
            branch_id=br
        )

# -------------------------------
# StudentBalances Testlari
# -------------------------------
class StudentBalancesModelTests(TestCase):
    def test_create_student_balance(self):
        org = Organizations.objects.create(name="Test Org")
        br = Branch.objects.create(organization_id=org, name="Main")
        student = Student.objects.create(
            organization_id=org,
            branch_id=br,
            full_name="Ali",
            phone_number="901234570",
            phone_number2="911234570",
            password="123456",
            address="Toshkent"
        )
        StudentBalances.objects.create(
            student=student,
            balance=Decimal("1500000"),
            organization_id=org,
            branch_id=br
        )

# -------------------------------
# StudentTransactions Testlari
# -------------------------------
class StudentTransactionsModelTests(TestCase):
    def test_create_student_transaction(self):
        org = Organizations.objects.create(name="Test Org")
        br = Branch.objects.create(organization_id=org, name="Main")
        student = Student.objects.create(
            organization_id=org,
            branch_id=br,
            full_name="Ali",
            phone_number="901234580",
            phone_number2="911234580",
            password="123456",
            address="Toshkent"
        )
        group = Group.objects.create(
            organization_id=org,
            branch_id=br,
            name="Python Backend",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 6, 1)
        )
        student_group = StudentGroup.objects.create(
            student=student,
            group=group,
            organization_id=org,
            branch_id=br,
            joined_at=date(2025, 1, 1),
            left_at=date(2025, 6, 1),
            end_date=date(2025, 6, 1)
        )
        employee = create_employee(org, br, username="employee_transaction")
        StudentTarnsactions.objects.create(
            student=student,
            student_group=student_group,
            group=group,
            transaction_type="payment",
            amount=Decimal("500000"),
            payment_type="cash",
            transaction_date=timezone.now(),
            accepted_by=employee,
            comment="Yanvar oyi to'lovi",
            organization_id=org,
            branch_id=br
        )

# -------------------------------
# StudentGroupLeaves Testlari
# -------------------------------
class StudentGroupLeavesTest(TestCase):
    def test_leave_creation(self):
        org = Organizations.objects.create(name="Test Org")
        br = Branch.objects.create(organization_id=org, name="Main")
        student = Student.objects.create(
            organization_id=org,
            branch_id=br,
            full_name="Ali",
            phone_number="901234590",
            phone_number2="911234590",
            password="123456",
            address="Toshkent"
        )
        group = Group.objects.create(
            organization_id=org,
            branch_id=br,
            name="Python",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 6, 1)
        )
        student_group = StudentGroup.objects.create(
            student=student,
            group=group,
            organization_id=org,
            branch_id=br,
            joined_at=date(2025, 1, 1),
            left_at=date(2025, 6, 1),
            end_date=date(2025, 6, 1)
        )
        leave_reason = LeaveReason.objects.create(
            name="Kasallik",
            organization_id=org,
            branch_id=br
        )
        employee = create_employee(org, br, username="employee_leave")
        StudentGroupLeaves.objects.create(
            student=student,
            group=group,
            student_group=student_group,
            leave_date=timezone.now(),
            leave_reason=leave_reason,
            refound_amount=Decimal("50000"),
            created_by=employee,
            organization_id=org,
            branch_id=br
        )

# -------------------------------
# StudentFreezes Testlari
# -------------------------------
class StudentFreezesTest(TestCase):
    def test_create_student_freeze(self):
        org = Organizations.objects.create(name="Test Org")
        br = Branch.objects.create(organization_id=org, name="Main")
        student = Student.objects.create(
            organization_id=org,
            branch_id=br,
            full_name="Ali",
            phone_number="901234600",
            phone_number2="911234600",
            password="123456",
            address="Toshkent"
        )
        group = Group.objects.create(
            organization_id=org,
            branch_id=br,
            name="Python",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 6, 1)
        )
        employee = create_employee(org, br, username="employee_freeze")
        StudentFreezes.objects.create(
            student=student,
            group=group,
            freeze_start_date=date(2025, 3, 1),
            freeze_end_date=date(2025, 3, 15),
            reason="Kasallik sababli",
            created_by=employee,
            organization_id=org,
            branch_id=br
        )

# -------------------------------
# StudentBalanceHistory Testlari
# -------------------------------
class StudentBalanceHistoryTest(TestCase):
    def test_create_balance_history(self):
        org = Organizations.objects.create(name="Test Org")
        br = Branch.objects.create(organization_id=org, name="Main")
        student = Student.objects.create(
            organization_id=org,
            branch_id=br,
            full_name="Ali",
            phone_number="901234610",
            phone_number2="911234610",
            password="123456",
            address="Toshkent"
        )
        StudentBalanceHistory.objects.create(
            student=student,
            amount=Decimal("500000"),
            base_price=Decimal("600000"),
            applied_price=Decimal("550000"),
            discount=Decimal("50000"),
            organization_id=org,
            branch_id=br
        )

# -------------------------------
# Attendence Testlari
# -------------------------------
class AttendenceTest(TestCase):
    def test_create_attendence(self):
        org = Organizations.objects.create(name="Test Org")
        br = Branch.objects.create(organization_id=org, name="Main")
        student = Student.objects.create(
            organization_id=org,
            branch_id=br,
            full_name="Ali",
            phone_number="901234620",
            phone_number2="911234620",
            password="123456",
            address="Toshkent"
        )
        group = Group.objects.create(
            organization_id=org,
            branch_id=br,
            name="Python",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 6, 1)
        )
        student_group = StudentGroup.objects.create(
            student=student,
            group=group,
            organization_id=org,
            branch_id=br,
            joined_at=date(2025, 1, 1),
            left_at=date(2025, 6, 1),
            end_date=date(2025, 6, 1)
        )
        employee = create_employee(org, br, username="employee_attendence")
        Attendence.objects.create(
            student_group=student_group,
            lesson_date=date(2025, 2, 10),
            is_present=True,
            marked_by=employee,
            organization_id=org,
            branch_id=br
        )


#  Serializer👇  bu yog'i


class StudentSerializerTest(TestCase):
    def test_student_serializer(self):
        org = Organizations.objects.create(name="Test Org")
        branch = Branch.objects.create(name="Main", organization_id=org)

        student = Student.objects.create(
            full_name="Ali Valiyev",
            phone_number="+998901234567",
            organization_id=org,
            branch_id=branch
        )

        serializer = StudentSerializer(student)
        serializer.data



class StudentGroupSerializerTest(TestCase):
    def test_student_group_serializer(self):
        serializer = StudentGroupSerializer


class StudentPricingSerializerTest(TestCase):
    def test_student_pricing_serializer(self):
        serializer = StudentPricingSerializer


class StudentBalancesSerializerTest(TestCase):
    def test_student_balances_serializer(self):
        serializer = StudentBalancesSerializer



class StudentTransactionsSerializerTest(TestCase):
    def test_student_transactions_serializer(self):
        serializer = StudentTransactionsSerializerTest


class LeaveReasonSerializerTest(TestCase):
    def test_leave_reason_serializer(self):
        serializer = LeaveReasonSerializer



class StudentGroupLeavesSerializerTest(TestCase):
    def test_group_leaves_serializer(self):
        serializer = StudentGroupLeavesSerializerTest



class StudentFreezesSerializerTest(TestCase):
    def test_student_freezes_serializer(self):
        serializer = StudentFreezesSerializer



class StudentBalanceHistorySerializerTest(TestCase):
    def test_balance_history_serializer(self):
        serializer = StudentBalanceHistorySerializer


class AttendenceSerializerTest(TestCase):
    def test_attendence_serializer(self):
        serializer = AttendenceSerializer


class RoomSerializerTest(TestCase):
    def test_room_serializer(self):
        serializer = RoomSerializer


class CourseSerializerTest(TestCase):
    def test_course_serializer(self):
        serializer = CourseSerializer


class GroupSerializerTest(TestCase):
    def test_group_serializer(self):
        serializer = GroupSerializer



class GroupTeacherSerializerTest(TestCase):
    def test_group_teacher_serializer(self):
        serializer = GroupTeacherSerializer



class LessonTimeSerializerTest(TestCase):
    def test_lesson_time_serializer(self):
        serializer = LessonTimeSerializer


class LessonScheduleSerializerTest(TestCase):
    def test_lesson_schedule_serializer(self):
        serializer = LessonScheduleSerializer


class ExamsSerializerTest(TestCase):
    def test_exams_serializer(self):
        serializer = ExamsSerializer


class ExamResultsSerializerTest(TestCase):
    def test_exam_results_serializer(self):
        serializer = ExamResultsSerializer


class TeacherSalaryRulesSerializerTest(TestCase):
    def test_salary_rules_serializer(self):
        serializer = TeacherSalaryRulesSerializer


class TeacherSalaryPaymentsSerializerTest(TestCase):
    def test_salary_payments_serializer(self):
        serializer = TeacherSalaryPaymentsSerializer


class TeacherSalaryCalculationsSerializerTest(TestCase):
    def test_salary_calculations_serializer(self):
        serializer = TeacherSalaryCalculationsSerializerTest






