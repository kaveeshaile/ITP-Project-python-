from django.db import models

# Create your models here.
    
    
class events(models.Model):
   Event_ID = models.AutoField(primary_key=True)
   Event_type = models.CharField(max_length=200)
   Location = models.CharField(max_length=100)
   Contact = models.CharField(max_length=100)
   Customer_ID = models.CharField(max_length=10)
   Date = models.DateField(blank=True, null=True)
   Status = models.CharField(max_length=100)
   OnCreateTime = models.DateTimeField(blank=True,null=True)
   class Meta:
     db_table = "event"
     
  
     
class reservations(models.Model):
   Reservation_ID = models.AutoField(primary_key=True)
   Event_ID = models.CharField(max_length=10)
   S_Time = models.DateTimeField(blank=True, null=True)
   E_Time = models.DateTimeField(blank=True, null=True)
   Resources_ID = models.CharField(max_length=10)
   Resources_Name = models.CharField(max_length=20)
   class Meta:
     db_table = "reservations"
     
     
     
class eventbin(models.Model):
   Event_ID = models.CharField(max_length=10, primary_key=True)
   Event_type = models.CharField(max_length=200)
   Location = models.CharField(max_length=100)
   Contact = models.CharField(max_length=100)
   Customer_ID = models.CharField(max_length=10)
   Date = models.DateField(blank=True, null=True)
   Status = models.CharField(max_length=100)
   OnCreateTime = models.DateTimeField(blank=True, null=True)
   class Meta:
     db_table = "completed_events"
     
     
    
class customer(models.Model):
   Customer_ID = models.AutoField(primary_key=True)
   F_name = models.CharField(max_length=40)
   L_name = models.CharField(max_length=50) 
   Email = models.CharField(max_length=100)
   Address = models.CharField(max_length=100)
   Phone = models.CharField(max_length=20)
   Username = models.CharField(max_length=20)
   Password = models.CharField(max_length=50)
   class Meta:
     db_table = "customer"
     
     
class admin_login(models.Model):
   admin_id = models.AutoField(primary_key=True)
   username = models.CharField(max_length=20)
   password = models.CharField(max_length=40)
   class Meta:
     db_table = "admin_login"
     