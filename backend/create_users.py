import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from users.models import Staff, Student
from django.contrib.auth.hashers import make_password

# Staff Users - 8 staff members
staff_users = [
    ("james_wilson", "Staff@123", "james.wilson@university.edu", "James", "Wilson", "Executive", "Executive Office", 1),
    ("maria_garcia", "Staff@456", "maria.garcia@university.edu", "Maria", "Garcia", "Operations Manager", "Operations", 2),
    ("david_park", "Staff@789", "david.park@university.edu", "David", "Park", "Campus Planner", "Planning", 3),
    ("lisa_rodriguez", "Staff@101", "lisa.rodriguez@university.edu", "Lisa", "Rodriguez", "Data Analyst", "Analytics", 4),
    ("kevin_zhang", "Staff@202", "kevin.zhang@university.edu", "Kevin", "Zhang", "Marketing Manager", "Marketing", 5),
    ("jose_garcia", "Staff@303", "jose.garcia@university.edu", "Jose", "Garcia", "Maintenance Technician", "Facilities", 6),
    ("lisa_thomas", "Staff@404", "lisa.thomas@university.edu", "Lisa", "Thomas", "Security Officer", "Security", 7),
    ("carlos_rodriguez", "Staff@505", "carlos.rodriguez@university.edu", "Carlos", "Rodriguez", "Kitchen Staff", "Food Services", 8),
]

# Student Users - 10 students
student_users = [
    ("alice_johnson", "Student@123", "alice.johnson@university.edu", "Alice", "Johnson", "S2024001", "Computer Science", 101),
    ("bob_smith", "Student@456", "bob.smith@university.edu", "Bob", "Smith", "S2024002", "Engineering", 102),
    ("carol_davis", "Student@789", "carol.davis@university.edu", "Carol", "Davis", "S2024003", "Mathematics", 103),
    ("david_wilson", "Student@101", "david.wilson@university.edu", "David", "Wilson", "S2024004", "Physics", 104),
    ("emma_brown", "Student@202", "emma.brown@university.edu", "Emma", "Brown", "S2024005", "Chemistry", 105),
    ("frank_miller", "Student@303", "frank.miller@university.edu", "Frank", "Miller", "S2024006", "Biology", 106),
    ("grace_lee", "Student@404", "grace.lee@university.edu", "Grace", "Lee", "S2024007", "Economics", 107),
    ("henry_taylor", "Student@505", "henry.taylor@university.edu", "Henry", "Taylor", "S2024008", "Psychology", 108),
    ("isabel_martin", "Student@606", "isabel.martin@university.edu", "Isabel", "Martin", "S2024009", "Sociology", 109),
    ("jack_anderson", "Student@707", "jack.anderson@university.edu", "Jack", "Anderson", "S2024010", "History", 110),
]

print("\n" + "="*60)
print("  STAFF USERS (8 Staff Members)")
print("="*60)

created_staff = 0
for username, password, email, first, last, role, dept, food_id in staff_users:
    if not Staff.objects.filter(email=email).exists():
        Staff.objects.create(
            username=username,
            password=make_password(password),
            email=email,
            first_name=first,
            last_name=last,
            role=role,
            department=dept,
            food_id=food_id
        )
        print(f"✅ Staff: {first} {last} - {role}")
        created_staff += 1

print("\n" + "="*60)
print("  STUDENT USERS (10 Students)")
print("="*60)

created_students = 0
for username, password, email, first, last, student_id, major, food_id in student_users:
    if not Student.objects.filter(email=email).exists():
        Student.objects.create(
            username=username,
            password=make_password(password),
            email=email,
            first_name=first,
            last_name=last,
            student_id=student_id,
            major=major,
            food_id=food_id
        )
        print(f"✅ Student: {first} {last} - {major}")
        created_students += 1

print("\n" + "="*60)
print("  SUMMARY")
print("="*60)
print(f"Staff created: {created_staff}/8")
print(f"Students created: {created_students}/10")
print("="*60)
