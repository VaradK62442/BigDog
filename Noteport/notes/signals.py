from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import NotesEnvironment
from account.models import UserProfile
 
@receiver(pre_delete, sender=UserProfile) 
def fix_ownership(sender, instance, **kwargs):
    notesEnvironments = NotesEnvironment.objects.filter(owner=instance)
        
    for noteEnvironment in notesEnvironments:
        admins = noteEnvironment.admins.all()
        if admins.exists():
            noteEnvironment.owner = admins[0]
            noteEnvironment.save()
        else:
            noteEnvironment.delete()