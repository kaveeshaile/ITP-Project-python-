from django.db import models

# Create your models here.

class video_add(models.Model):
 Name=models.CharField(max_length=100)
 Contact=models.CharField(max_length=10)
 ContactEmail=models.CharField(max_length=45)
 Description=models.CharField(max_length=200)
 Fee=models.CharField(max_length=45)
 class Meta:
    db_table = "videography"
    
class video_add2(models.Model):
 fee=models.CharField(max_length=45)
 class Meta:
    db_table = "child"