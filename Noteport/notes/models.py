from django.db import models
from account.models import UserProfile

class NotesEnvironment(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    admins = models.ManyToManyField(UserProfile)
    viewers = models.ManyToManyField(UserProfile)
    public = models.BooleanField(default=False)

    name = models.CharField()
    description = models.CharField()


#NoteEnvironment Blocks

class NotesPage(models.Model):
    notesEnvironment = models.ForeignKey(NotesEnvironment, on_delete=models.CASCADE)
    name = models.CharField()
    hidden = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)