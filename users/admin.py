from django.contrib import admin

# Register your models here.
from .models import Profile, StudentStats

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'username', 'email', 'user_type', 'id')
    list_filter = ('user_type',)
    search_fields = ('name', 'username', 'email')
    list_per_page = 100

class StudentStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name','category','subcategory','score','total_questions','score_percentage', 'is_enabled','id')

admin.site.register(StudentStats, StudentStatsAdmin)
admin.site.register(Profile, ProfileAdmin)
