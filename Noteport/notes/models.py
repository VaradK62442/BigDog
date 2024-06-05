from django.db import models
from account.models import UserProfile

class NotesEnvironment(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    admins = models.ManyToManyField(UserProfile, related_name="administrates")
    collaborator = models.ManyToManyField(UserProfile, related_name="collaborates")
    public = models.BooleanField(default=False)

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

#NoteEnvironment Blocks

class NotesPage(models.Model):
    notesEnvironment = models.ForeignKey(NotesEnvironment, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    hidden = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)