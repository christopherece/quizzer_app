
from django.contrib import admin
from .models import Category, Subcategory, Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)




admin.site.register(Option)
