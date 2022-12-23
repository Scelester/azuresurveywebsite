from django.contrib import admin

# Register your models here.
from survey.models import Survey_answers,Survey_questions
admin.site.register(Survey_answer)
admin.site.register(Survey_question)