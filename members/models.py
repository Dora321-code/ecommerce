from django.db import models

class Member(models.Model):
  username = models.CharField(max_length=50, default='name_surname')
  email = models.EmailField(unique=True, default='name@gmail.com')
  password_hash = models.CharField(max_length=100, default='harsh123')
  full_name = models.CharField(max_length=100, blank=True, null=True)
  registration_date = models.DateTimeField(default='2000-01-01T00:00:00Z')
class Session(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    session_token = models.CharField(max_length=100)
    expiry_timestamp = models.DateTimeField()