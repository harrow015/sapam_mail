from django.db import models
from site_admin.models import *

# Create your models here.
class country_table(models.Model):
    country_name=models.CharField(max_length=20)
    
   
class state_table(models.Model):
    state_name=models.CharField(max_length=20)
    country_id=models.ForeignKey(country_table, on_delete=models.CASCADE) 
    
    

class register_table(models.Model):
    name=models.CharField(max_length=20) 
    gender=models.CharField(max_length=20)    
    dob=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    securityquestion=models.CharField(max_length=20)
    answer=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    country_id=models.ForeignKey(country_table, on_delete=models.CASCADE)
    state_id=models.ForeignKey(state_table, on_delete=models.CASCADE)
    
class hobbie_table(models.Model):
    userid=models.ForeignKey(register_table, on_delete=models.CASCADE)
    hobbyid=models.ForeignKey('site_admin.hobby_table',on_delete=models.CASCADE)
    
class message_table(models.Model):
    senderid=models.ForeignKey(register_table,on_delete=models.CASCADE,related_name='senderid') 
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=20)
    date=models.CharField(max_length=20)   
    time=models.CharField(max_length=20)
    reciverid=models.ForeignKey(register_table,on_delete=models.CASCADE,related_name='reciverid')
    status=models.CharField(max_length=20,default="pending")
    filterstatus=models.CharField(max_length=20,default="pending")

class trash_table(models.Model):
    msgid=models.ForeignKey(message_table, on_delete=models.CASCADE,related_name='msgid')
    userid=models.ForeignKey(register_table,on_delete=models.CASCADE,related_name='userid')
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)    
    