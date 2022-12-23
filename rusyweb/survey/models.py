from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Survey_questions(models.Model):
    question = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Survey_answers(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Survey_questions, on_delete=models.CASCADE``) 
    answer = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer