from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'username', 'email', 'user_type', 'id')
    list_filter = ('user_type',)
    search_fields = ('name', 'username', 'email')
    list_per_page = 100

admin.site.register(Profile, ProfileAdmin)
