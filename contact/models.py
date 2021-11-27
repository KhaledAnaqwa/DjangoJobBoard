import email
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

 
class Info (models.Model):
    place=models.CharField(max_length=200)
    phoneNumber=PhoneNumberField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
