from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
  # Following change makes the “Publication date” comes before the “Question” field
  fieldsets = [
    (None, {"fields": ["question_text"]}),
    ("Date information", {"fields": ["pub_date"]})
  ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
