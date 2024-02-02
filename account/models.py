from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name
    # last_name
    # email
    # date_joined
    phone_number = models.IntegerField()

    def __str__(self):
        return str(self.user)