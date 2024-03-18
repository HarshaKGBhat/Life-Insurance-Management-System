from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



    
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Customer/',null=True,blank=True)
    address = models.CharField(max_length=40)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{6,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    mobile = models.CharField(max_length=20)
    salary=models.IntegerField(null=False)
    occupation=models.CharField(max_length=30,null=False)
    DOB=models.DateField(null=False)
    familymembers=models.IntegerField(null=False) 
    
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name