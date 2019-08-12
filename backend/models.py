from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

class Profile(User):
    profile=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user',parent_link=True)
    mobile=models.CharField(max_length=10)
    active_plan=models.CharField(max_length=50)

    def __str__(self):
        return self.username