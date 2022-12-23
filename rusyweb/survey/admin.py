from django.contrib import admin

# Register your models here.
from survey.models import Survey_answers,Survey_questions
admin.site.register(Survey_answers)
admin.site.register(Survey_questions)