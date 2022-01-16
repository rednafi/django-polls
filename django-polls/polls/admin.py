from django.contrib import admin

from . import models


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_published_recently")
    search_fields = ["question_text"]
    list_filter = ["pub_date"]


admin.site.register(models.Question, QuestionAdmin)
