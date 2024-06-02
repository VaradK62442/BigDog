from django.db import models
from notes.models import NotesEnvironment

# Standard Quiz

class StandardQuiz(models.Model):
    notesEnvironment = models.ForeignKey(NotesEnvironment, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

# Question Types

class MultipleChoiceQuestion(models.Model):
    quiz = models.ForeignKey(StandardQuiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=128)
    option1 = models.CharField(max_length=128)
    option2 = models.CharField(max_length=128)
    option3 = models.CharField(max_length=128)
    option4 = models.CharField(max_length=128)
    answer = models.IntegerField(default=1)

class TrueFalseQuestion(models.Model):
    quiz = models.ForeignKey(StandardQuiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=128)
    answer = models.BooleanField(default=False)