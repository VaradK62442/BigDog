import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Noteport.settings")

import django
django.setup()
from account.models import UserProfile
from django.contrib.auth.models import User

import json
import datetime
import random
random.seed(413)

def addUser(username, password, firstName, lastName, emailAddress, profilePicture, isStaff=False):
    user = User.objects.create_user(
        username = username,
        first_name = firstName,
        last_name = lastName,
        password = password,
        email = emailAddress,
    )
    user.is_staff = isStaff
    user.is_superuser = isStaff
    user.save()
    userProfile = UserProfile.objects.get_or_create(
        user = user,
        picture = profilePicture
    )[0]
    userProfile.save()
    return userProfile

def populate():
    addUser(
        'root', 'toor', 'Root', 'User',
        'root@gmail.com', '',
        isStaff=True
    )

def main():
    populate()

if __name__ == '__main__':
    main()