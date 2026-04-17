def test_user_creation(user):
  assert user.username is "john doe"
  assert user.password != "psswrd123"