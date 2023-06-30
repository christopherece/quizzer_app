from django.contrib import admin
from .models import Question
from .models import Option
from .models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

admin.site.register(Category, CategoryAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'explanation',
        'photo_main',
        'category','cat',


    )
admin.site.register(Question, QuestionAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'question_id',
        'question',
        'text',
        'is_correct',
    )
admin.site.register(Option, OptionAdmin)