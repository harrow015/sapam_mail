from django.db import models

# Create your models here.
class admin_table(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
class hobby_table(models.Model):
    hobbyname=models.CharField(max_length=20) 
    
class hobbyfactor_table(models.Model):
    factor_name=models.CharField(max_length=20)
    hobbyid=models.ForeignKey(hobby_table,on_delete=models.CASCADE)       
    
class season_table(models.Model):
    season_name=models.CharField(max_length=20)
    
class seasonfactor_table(models.Model):
    factor_name=models.CharField(max_length=20)
    seasonid=models.ForeignKey(season_table,on_delete=models.CASCADE)
            