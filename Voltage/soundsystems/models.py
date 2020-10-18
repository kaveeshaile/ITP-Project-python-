from django.db import models

# Create your models here.


class sound_admin(models.Model):

    id = models.CharField(max_length=10, primary_key=True)     
    Package_name=models.CharField(max_length=500)
    Suitable_for=models.CharField(max_length=500)
    Brand=models.CharField(max_length=500)
    Price=models.CharField(max_length=500)
    Description=models.CharField(max_length=2500)
    class Meta:
        db_table = "soundsystem"



        