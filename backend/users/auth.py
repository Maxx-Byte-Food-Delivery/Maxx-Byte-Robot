"""Authentication helpers."""
def has_permission(user, permission):
    if not user:
        return False
    if user.role == 'admin':
        return True
    permissions = {
        'student': ['view_own_profile', 'view_own_orders'],
        'staff': ['view_all_orders', 'view_user_profiles', 'search_logs'],
        'admin': ['*']
    }
    perms = permissions.get(user.role, [])
    return permission in perms or '*' in perms
