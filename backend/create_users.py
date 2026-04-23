import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from users.models import Staff, Student
from django.contrib.auth.hashers import make_password

# Staff Users - 8 roles (@university.edu)
staff_users = [
    ("robert_chen", "Staff@123", "robert.chen@university.edu", "Robert", "Chen", "Executive", "Executive Office", 1),
    ("sarah_morris", "Staff@123", "sarah.morris@university.edu", "Sarah", "Morris", "Operations Manager", "Operations", 2),
    ("david_kim", "Staff@123", "david.kim@university.edu", "David", "Kim", "Campus Planner", "Planning", 3),
    ("jessica_wong", "Staff@123", "jessica.wong@university.edu", "Jessica", "Wong", "Data Analyst", "Analytics", 4),
    ("michael_brown", "Staff@123", "michael.brown@university.edu", "Michael", "Brown", "Marketing Manager", "Marketing", 5),
    ("jose_garcia", "Staff@123", "jose.garcia@university.edu", "Jose", "Garcia", "Maintenance Technician", "Facilities", 6),
    ("lisa_thomas", "Staff@123", "lisa.thomas@university.edu", "Lisa", "Thomas", "Security Officer", "Security", 7),
    ("carlos_rodriguez", "Staff@123", "carlos.rodriguez@university.edu", "Carlos", "Rodriguez", "Kitchen Staff", "Food Services", 8),
]

# Student Users - 10 students (@university.edu)
student_users = [
    ("alice_johnson", "Student@123", "alice.johnson@university.edu", "Alice", "Johnson", "S2024001", "Computer Science", 101),
    ("bob_smith", "Student@123", "bob.smith@university.edu", "Bob", "Smith", "S2024002", "Engineering", 102),
    ("carol_davis", "Student@123", "carol.davis@university.edu", "Carol", "Davis", "S2024003", "Mathematics", 103),
    ("david_wilson", "Student@123", "david.wilson@university.edu", "David", "Wilson", "S2024004", "Physics", 104),
    ("emma_brown", "Student@123", "emma.brown@university.edu", "Emma", "Brown", "S2024005", "Chemistry", 105),
    ("frank_miller", "Student@123", "frank.miller@university.edu", "Frank", "Miller", "S2024006", "Biology", 106),
    ("grace_lee", "Student@123", "grace.lee@university.edu", "Grace", "Lee", "S2024007", "Economics", 107),
    ("henry_taylor", "Student@123", "henry.taylor@university.edu", "Henry", "Taylor", "S2024008", "Psychology", 108),
    ("isabel_martin", "Student@123", "isabel.martin@university.edu", "Isabel", "Martin", "S2024009", "Sociology", 109),
    ("jack_anderson", "Student@123", "jack.anderson@university.edu", "Jack", "Anderson", "S2024010", "History", 110),
]

print("\n" + "="*60)
print("  STAFF DATABASE (8 Roles)")
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
        print(f"✅ {first} {last} - {role} ({email})")
        created_staff += 1

print("\n" + "="*60)
print("  STUDENT DATABASE (10 Students)")
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
        print(f"✅ {first} {last} - {major} ({email})")
        created_students += 1

print("\n" + "="*60)
print("  SUMMARY")
print("="*60)
print(f"📊 Staff: {created_staff}/8")
print(f"📚 Students: {created_students}/10")
print(f"📧 All emails: @university.edu")
print("="*60)
# Updated: Thu Apr 23 17:42:42 EDT 2026
