from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
  model = Choice
  extra = 3       # <- Tells Django to provide enough fields for 3 choices, by default

class QuestionAdmin(admin.ModelAdmin):
  # Following change makes the “Publication date” comes before the “Question” field
  fieldsets = [
    (None, {"fields": ["question_text"]}),
    ("Date information", {"fields": ["pub_date"]}, {"classes": ["collapse"]})
  ]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
