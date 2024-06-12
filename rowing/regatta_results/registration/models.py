from django.db import models
from django.contrib.auth.models import User

#class for the diffrent users(Rowers, coaches, and officials)
class Profile(models.Model):
    USER_TYPES = (
        ("Rower", "Rower"),
        ("Official", "Official"),
        ("Coach", "Coach"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=15, choices=USER_TYPES)


def __str__(self):
    return f"{self.user.username} Profile"
