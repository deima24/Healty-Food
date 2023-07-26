from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


Avon = 'Avon'
Bedfordshire = 'Bedfordshire'
Berkshire = 'Berkshire'
Cambridgeshire = 'Cambridgeshire'
Buckinghamshire = 'Buckinghamshire'
Cheshire = 'Cheshire'
Cornwall = 'Cornwall'
Cumbria = 'Cumbria'
Derbyshire = 'Derbyshire'
Devon = 'Devon'
Dorset = 'Dorset'
Durham = 'Durham'
Essex = 'Essex'
Gloucestershire = 'Gloucestershire'
Hampshire = 'Hampshire'
Herefordshire = 'Herefordshire'
Hertfordshire = 'Hertfordshire'
Kent = 'Kent'
Lancashire = 'Lancashire'


COUNTIES = [
    (Avon, 'Avon'),
    (Bedfordshire, 'Bedfordshire'),
    (Berkshire, 'Berkshire'),
    (Cambridgeshire, 'Cambridgeshire'),
    (Buckinghamshire, 'Buckinghamshire'),
    (Cheshire, 'Cheshire'),
    (Cornwall, 'Cornwall'),
    (Cumbria, 'Cumbria'),
    (Derbyshire, 'Derbyshire'),
    (Devon, 'Devon'),
    (Dorset, 'Dorset'),
    (Durham, 'Durham'),
    (Essex, 'Essex'),
    (Gloucestershire, 'Gloucestershire'),
    (Hampshire, 'Hampshire'),
    (Herefordshire, 'Herefordshire'),
    (Hertfordshire, 'Hertfordshire'),
    (Kent, 'Kent'),
    (Lancashire, 'Lancashire'),
]


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    contact information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True,
        choices=COUNTIES)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
        instance.userprofile.save()
