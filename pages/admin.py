
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
    list_display = ('name','category','is_active','exam_date','exam_time')
    list_editable = ['is_active','exam_date','exam_time']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Superuser can see all categories
            return qs
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:  # If created_by is a ForeignKey to User model
            obj.created_by = request.user
        obj.save()

    def add_view(self, request, form_url='', extra_context=None):
        data = request.GET.copy()
        data.update({'created_by': request.user.pk})  # Set the default created_by
        request.GET = data
        return super().add_view(request, form_url, extra_context)


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]
    list_display = ('name','created_by','is_active')
    list_editable = ['is_active']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Superuser can see all categories
            return qs
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:  # If created_by is a ForeignKey to User model
            obj.created_by = request.user
        obj.save()

    def add_view(self, request, form_url='', extra_context=None):
        data = request.GET.copy()
        data.update({'created_by': request.user.pk})  # Set the default created_by
        request.GET = data
        return super().add_view(request, form_url, extra_context)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('text','category','subcategory')
    list_filter = ('category','subcategory')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(created_by=request.user)
        elif db_field.name == "subcategory":
            kwargs["queryset"] = Subcategory.objects.filter(created_by=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Superuser can see all questions
            return qs
        return qs.filter(subcategory__created_by=request.user)


class OptionAdmin(admin.ModelAdmin):
    list_display = ('text','is_correct','question')


# class QuizAttemptAdmin(admin.ModelAdmin):
#     list_display = ('user','subcategory')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(QuizAttempt, QuizAttemptAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
# admin.site.register(Option)
