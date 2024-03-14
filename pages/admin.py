
from django.contrib import admin
from .models import Category, Subcategory, Question, Option, QuizAttempt

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1
    
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name','category','is_active')
    list_editable = ['is_active']


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]
    list_filter = ('name','created_by','is_active')
    list_display = ('name','created_by','is_active')
    list_editable = ['is_active']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user','subcategory')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizAttempt, QuizAttemptAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)




admin.site.register(Option)
