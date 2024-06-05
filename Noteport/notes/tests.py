from django.test import TestCase
from .models import NotesEnvironment
from account.models import UserProfile
from django.contrib.auth.models import User

class EnvironmentDeletion(TestCase):

    def test_person_owns_no_environments(self):
        self.person1 = User.objects.create(username='TestOwner', email='owner@gmail.com')
        self.owner = UserProfile.objects.create(user=self.person1)
        self.person1.delete()
    
    def test_admin_exist(self):
        self.person1 = User.objects.create(username='TestOwner', email='owner@gmail.com')
        self.person2 = User.objects.create(username='TestAdmin', email='admin@gmail.com')
        self.owner = UserProfile.objects.create(user=self.person1)
        self.admin = UserProfile.objects.create(user=self.person2)
        self.noteEnvironment = NotesEnvironment.objects.create(owner=self.owner,name="NotDeleted")
        self.noteEnvironment.admins.add(self.admin)
        self.person1.delete()
        self.assertTrue(NotesEnvironment.objects.filter(name="NotDeleted").exists())
        self.assertEqual(NotesEnvironment.objects.get(name="NotDeleted").owner, self.admin)

    def test_no_admins_exist(self):
        self.person1 = User.objects.create(username='TestOwner', email='owner@gmail.com')
        self.owner = UserProfile.objects.create(user=self.person1)
        self.noteEnvironment = NotesEnvironment.objects.create(owner=self.owner,name="Deleted")
        self.person1.delete()
        self.assertFalse(NotesEnvironment.objects.filter(name="Deleted").exists())

    def test_admins_exist(self):
        self.person1 = User.objects.create(username='TestOwner', email='owner@gmail.com')
        self.person2 = User.objects.create(username='TestAdmin1', email='admin1@gmail.com')
        self.person3 = User.objects.create(username='TestAdmin2', email='admin2@gmail.com')
        self.owner = UserProfile.objects.create(user=self.person1)
        self.admin1 = UserProfile.objects.create(user=self.person2)
        self.admin2 = UserProfile.objects.create(user=self.person3)
        self.noteEnvironment = NotesEnvironment.objects.create(owner=self.owner,name="NotDeleted")
        self.noteEnvironment.admins.add(self.admin1, self.admin2)
        self.person1.delete()
        self.assertTrue(NotesEnvironment.objects.filter(name="NotDeleted").exists())
        self.assertEqual(NotesEnvironment.objects.get(name="NotDeleted").owner, self.admin1)

    def test_owner_of_multiple(self):
        self.person1 = User.objects.create(username='TestOwner', email='owner@gmail.com')
        self.person2 = User.objects.create(username='TestAdmin1', email='admin1@gmail.com')
        self.person3 = User.objects.create(username='TestAdmin2', email='admin2@gmail.com')
        self.owner = UserProfile.objects.create(user=self.person1)
        self.admin1 = UserProfile.objects.create(user=self.person2)
        self.admin2 = UserProfile.objects.create(user=self.person3)
        self.noteEnvironment1 = NotesEnvironment.objects.create(owner=self.owner,name="NotDeleted")
        self.noteEnvironment1.admins.add(self.admin1, self.admin2)
        self.noteEnvironment2 = NotesEnvironment.objects.create(owner=self.owner,name="Deleted")
        self.person1.delete()
        self.assertTrue(NotesEnvironment.objects.filter(name="NotDeleted").exists())
        self.assertFalse(NotesEnvironment.objects.filter(name="Deleted").exists())
        self.assertEqual(NotesEnvironment.objects.get(name="NotDeleted").owner, self.admin1)