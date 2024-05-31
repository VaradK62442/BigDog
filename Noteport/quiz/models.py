from django.db import models
from notes.models import NotesEnvironment

# Standard Quiz

class StandardQuiz(models.Model):
    notesEnvironment = models.ForeignKey(NotesEnvironment, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.CharField()

# Question Types

class MultipleChoiceQuestion(models.Model):
    quiz = models.ForeignKey(StandardQuiz, on_delete=models.CASCADE)
    question = models.CharField()
    option1 = models.CharField()
    option2 = models.CharField()
    option3 = models.CharField()
    option4 = models.CharField()
    answer = models.IntegerField(default=1)

class TrueFalseQuestion(models.Model):
    quiz = models.ForeignKey(StandardQuiz, on_delete=models.CASCADE)
    question = models.CharField()
    answer = models.BooleanField()