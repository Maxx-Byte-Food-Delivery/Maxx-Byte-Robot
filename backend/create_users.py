import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Define roles and their users with university.edu emails
users_with_roles = [
    # Executive
    ("ceo_john", "Executive@123", "ceo_john@university.edu", "John", "Smith", "Executive"),
    
    # Operations managers
    ("op_mgr_sarah", "Ops@123", "sarah.johnson@university.edu", "Sarah", "Johnson", "Operations Manager"),
    ("op_mgr_mike", "Ops@456", "mike.williams@university.edu", "Mike", "Williams", "Operations Manager"),
    
    # Campus planners
    ("campus_planner_emily", "Plan@123", "emily.brown@university.edu", "Emily", "Brown", "Campus Planner"),
    ("campus_planner_david", "Plan@456", "david.jones@university.edu", "David", "Jones", "Campus Planner"),
    
    # Data analysts
    ("data_analyst_lisa", "Data@123", "lisa.garcia@university.edu", "Lisa", "Garcia", "Data Analyst"),
    ("data_analyst_tom", "Data@456", "tom.martinez@university.edu", "Tom", "Martinez", "Data Analyst"),
    
    # Marketing managers
    ("marketing_mgr_jessica", "Mktg@123", "jessica.rodriguez@university.edu", "Jessica", "Rodriguez", "Marketing Manager"),
    ("marketing_mgr_ryan", "Mktg@456", "ryan.lee@university.edu", "Ryan", "Lee", "Marketing Manager"),
    
    # Maintenance technicians
    ("maint_tech_chris", "Maint@123", "chris.walker@university.edu", "Chris", "Walker", "Maintenance Technician"),
    ("maint_tech_pat", "Maint@456", "pat.hall@university.edu", "Pat", "Hall", "Maintenance Technician"),
    
    # Campus security officers
    ("security_james", "Secure@123", "james.young@university.edu", "James", "Young", "Campus Security Officer"),
    ("security_maria", "Secure@456", "maria.king@university.edu", "Maria", "King", "Campus Security Officer"),
    
    # Kitchen staff
    ("kitchen_chef_tony", "Kitchen@123", "tony.wright@university.edu", "Tony", "Wright", "Kitchen Staff Member"),
    ("kitchen_assist_linda", "Kitchen@456", "linda.scott@university.edu", "Linda", "Scott", "Kitchen Staff Member"),
]

# Original test users (as regular students/faculty with university.edu emails)
regular_users = [
    ("alice_johnson", "Alice@123", "alice.johnson@university.edu", "Alice", "Johnson", "Student"),
    ("bob_smith", "Bob@456", "bob.smith@university.edu", "Bob", "Smith", "Student"),
    ("carol_davis", "Carol@789", "carol.davis@university.edu", "Carol", "Davis", "Faculty"),
    ("david_wilson", "David@101", "david.wilson@university.edu", "David", "Wilson", "Student"),
    ("emma_brown", "Emma@202", "emma.brown@university.edu", "Emma", "Brown", "Faculty"),
    ("frank_miller", "Frank@303", "frank.miller@university.edu", "Frank", "Miller", "Student"),
    ("grace_lee", "Grace@404", "grace.lee@university.edu", "Grace", "Lee", "Faculty"),
    ("henry_taylor", "Henry@505", "henry.taylor@university.edu", "Henry", "Taylor", "Student"),
    ("isabel_martin", "Isabel@606", "isabel.martin@university.edu", "Isabel", "Martin", "Faculty"),
    ("jack_anderson", "Jack@707", "jack.anderson@university.edu", "Jack", "Anderson", "Student"),
]

# Combine all users
all_users = users_with_roles + regular_users

created = 0
existing = 0

for username, password, email, first, last, role in all_users:
    if not User.objects.filter(username=username).exists():
        User.objects.create(
            username=username,
            password=make_password(password),
            email=email,
            first_name=first,
            last_name=last
        )
        print(f"✓ Created: {username} ({role}) - {email}")
        created += 1
    else:
        print(f"○ Exists: {username}")
        existing += 1

print(f"\n{'='*50}")
print(f"Summary: {created} new users created, {existing} already exist")
print(f"Total users with university.edu emails: {created + existing}")
print(f"{'='*50}")
