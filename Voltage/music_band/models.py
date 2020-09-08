from django.db import models

# Create your models here.

class music_band_package_add(models.Model):
 Package=models.CharField(max_length=100)
 No of songs=models.CharField(max_length=10)
 Charging rate=models.CharField(max_length=45)
 Description=models.CharField(max_length=200)
 Other Details=models.CharField(max_length=200)
 class Meta:
    db_table = "music_band"
    
class music_band_package_add(models.Model):
 fee=models.CharField(max_length=45)
 class Meta:
    db_table = "child"