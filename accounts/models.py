from email.mime import image
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
def upload(instance , filename):
    name,ext= filename.split(".")
    import time
    milliseconds = str(int(round(time.time() * 1000)))
    return f"profile/{instance.id}/{milliseconds+'.'+ ext}"


class Profile(models.Model):
    user=models.OneToOneField(User,related_name="User_Profile",on_delete=CASCADE)
    city=models.ForeignKey('City',related_name="Profile_City",on_delete=CASCADE ,blank=True ,null=True)
    phoneNumber=PhoneNumberField()
    image = models.ImageField(upload_to=upload)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    


class City(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
