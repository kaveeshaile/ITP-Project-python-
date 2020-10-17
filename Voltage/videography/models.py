from django.db import models

# Create your models here.

class video_add(models.Model):
 id = models.CharField(max_length=10, primary_key=True)     
 Name=models.CharField(max_length=100)
 Contact=models.CharField(max_length=10)
 ContactEmail=models.CharField(max_length=45)
 Description=models.CharField(max_length=1200)
 Fee=models.CharField(max_length=45)
 profile_pic = models.ImageField(null = True,blank = True,upload_to = "samples")
 class Meta:
    db_table = "videography"
    
    
class video_samples(models.Model):
       Resources_ID = models.CharField(max_length=20, primary_key=True)
       Samples = models.FileField(null = True, blank = True, upload_to="samples", max_length=100)
       class Meta:
              db_table = "video_samples"
    
    
    
class resources(models.Model):
   Resources_ID = models.CharField(max_length=40,primary_key=True)
   Status = models.CharField(max_length=40)
   Admin_ID = models.CharField(max_length=40)
   Facility_ID = models.CharField(max_length=40)
   class Meta:
    db_table = "resources"
    