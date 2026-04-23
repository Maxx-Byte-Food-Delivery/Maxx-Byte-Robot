import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from users.models import Staff, Student
from django.contrib.auth.hashers import make_password

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
print("  STAFF USERS")
print("="*60)
for u in staff_users:
    if not Staff.objects.filter(email=u[2]).exists():
        Staff.objects.create(username=u[0], password=make_password(u[1]), email=u[2], first_name=u[3], last_name=u[4], role=u[5], department=u[6], food_id=u[7])
        print(f"✅ Staff: {u[3]} {u[4]}")

print("\n" + "="*60)
print("  STUDENT USERS")
print("="*60)
for u in student_users:
    if not Student.objects.filter(email=u[2]).exists():
        Student.objects.create(username=u[0], password=make_password(u[1]), email=u[2], first_name=u[3], last_name=u[4], student_id=u[5], major=u[6], food_id=u[7])
        print(f"✅ Student: {u[3]} {u[4]}")

print("\n✅ Done!")
