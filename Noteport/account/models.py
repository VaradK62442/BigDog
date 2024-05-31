from django.db import models
from django.contrib.auth.models import User
from notes.models import NotesEnvironment

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures', blank=True)
    
    def delete(self):
        notesEnvironments = NotesEnvironment.objects.filter(owner=self)
        
        #For all owned note environments, change ownership if an admin exists, else delete
        for noteEnvironment in notesEnvironments:
            admins = noteEnvironment.admins
            if admins.exists():
                noteEnvironment.owner = admins[0]
                noteEnvironment.save()
            else:
                noteEnvironment.delete()

        super(UserProfile, self).delete()