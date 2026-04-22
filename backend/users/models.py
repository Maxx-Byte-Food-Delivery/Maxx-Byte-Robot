"""User models for student/staff/admin roles."""
from datetime import datetime

class User:
    def __init__(self, id, username, email, role, first_name, last_name):
        self.id = id
        self.username = username
        self.email = email
        self.role = role  # student, staff, admin
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = True
        self.created_at = datetime.now()
