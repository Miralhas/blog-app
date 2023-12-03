from django.contrib import admin
from accounts.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "is_staff"]
    list_filter = ["is_staff"]


admin.site.register(User, UserAdmin)
