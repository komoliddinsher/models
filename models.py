from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass



class Lead(models.Model):
    ismi=models.CharField(max_length=30)
    familiyasi=models.CharField(max_length=30)
    yoshi=models.IntegerField(default=0)
    malumoti=models.CharField(max_length=30)

    agent=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.ismi)



       

class Agent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)




# Create your models here.
