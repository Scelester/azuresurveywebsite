from django.contrib import admin

# Register your models here.
from survey.models import Survey_answer,Survey_question
admin.site.register(Survey_answer)
admin.site.register(Survey_question)