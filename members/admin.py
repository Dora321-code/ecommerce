from django.contrib import admin

# Register your models here.
from .models import Member, Session

admin.site.register(Member)
admin.site.register(Session)