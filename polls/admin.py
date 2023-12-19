from django.contrib import admin

# Register your models here.
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
  # Following change makes the “Publication date” comes before the “Question” field
  fields = ["pub_date", "question_text"]

admin.site.register(Question)
