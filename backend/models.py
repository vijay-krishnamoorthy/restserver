from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,UserManager
import datetime

# Create your models here.
class User(AbstractUser):
    mobile=models.CharField(max_length=11,unique=True)
    email=models.EmailField(unique=True)
    date_joined=models.DateField(default=datetime.date.today)
    USERNAME_FIELD='mobile'
    REQUIRED_FIELDS=('username','password','email')
    def __str__(self):
        return self.username
    object=UserManager()


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self,mobile,email, username, password=None):
        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username,mobile, password):
        user = self.create_user(
            email,
            password=password,
            username=username,
            mobile=mobile
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, mobile, password):
        user = self.create_user(
            email,
            password=password,
            mobile=mobile,
            username=username,
            name= "True",
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class Profile(User):
    profile=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user',parent_link=True)

    def __str__(self):
        return self.username

class Prepaidplans(models.Model):
    planname=models.CharField(max_length=100)
    planprice=models.FloatField()
    planduration=models.IntegerField()
    plandes=models.TextField()
    
    class Meta:
        ordering=("planprice",) #-planprice for reverse order #tuple so ,
    def __str__(self):
        return self.planname #display names in the admin panel

class Dashboard(Profile):
    dashboardprofile=models.OneToOneField(Profile,on_delete=models.CASCADE,related_name='dashboard',parent_link=True)
    # active_plan=models.OneToOneField(Prepaidplans, on_delete=models.CASCADE,related_name='prepaidplans',parent_link=True)
    active_plan=models.CharField(max_length=150,default="No active plan")
    plan_type=models.CharField(max_length=50,blank=True,null=True)
    voice_usage=models.CharField(max_length=100,blank=True,null=True)
    data_usage=models.CharField(max_length=100,blank=True,null=True)
    balance=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=1000,blank=True,null=True)
    pincode=models.CharField(max_length=100,blank=True,null=True)

class Inquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recharge(models.Model):
    mobile=models.CharField(max_length=10) 
    amount=models.CharField(max_length=10)  
    rdate=models.CharField(max_length=50)
    pid=models.CharField(max_length=10)

    def __str__(self):
        return self.mobile

class Dongleplans(models.Model):
    planname=models.CharField(max_length=100)
    data=models.CharField(max_length=10)
    validity=models.CharField(max_length=10)
    price=models.CharField(max_length=10)

    class Meta:
        ordering=('price',)
        verbose_name='Dongleplan'
    
    def __str__(self):
        return self.planname #display names in the admin panel

class Feedback(models.Model):
    fname=models.CharField(max_length=100)
    femail=models.CharField(max_length=100)
    fsubject=models.CharField(max_length=100)
    fmessage=models.CharField(max_length=1000)



class Preform(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)
    num=models.CharField(max_length=10)

    class Meta:
        ordering=('name',)
        verbose_name='Preform'
    
    def __str__(self):
        return self.name

class Postform(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)
    num=models.CharField(max_length=10)
    class Meta:
        ordering=('name',)
        verbose_name='Postform'
    
    def __str__(self):
        return self.name

class Dongleform(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=10)
    pincode=models.CharField(max_length=6)

    class Meta:
        ordering=('name',)
        verbose_name='Dongleform'
    
    def __str__(self):
        return self.name