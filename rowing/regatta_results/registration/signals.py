from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def make_profile(sender, instance, created, **kwargs): #call this whenever new User obj is saved
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): #function to save New user
    instance.profile.save()
