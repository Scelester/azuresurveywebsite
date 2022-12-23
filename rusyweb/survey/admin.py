from django.contrib import admin

# Register your models here.
from survey.models import Survey_answers,Survey_questions
admin.register(Survey_answers)
admin.register(Survey_questions)