from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

class usermanager(BaseUserManager):
    #contains all the operations related functions on th account class
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have an email adress")
        user=self.model(email=self.normalize_email(email),
        username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password=None):
        user=self.create_user(email,password=password,username=username)
        user.is_admin=True
        user.is_staff=True
        user.save(using=self._db)
        return user




class account(AbstractBaseUser):
    #account class contains all the information unique to user
    #the point of using custom model is to contain most of the information
    #in one model to avoid complex queries
    email=models.EmailField(max_length=60,unique=True)
    username=models.CharField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    objects=usermanager()

    def get_username(self):
        return self.email

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

    




    




# Create your models here.
