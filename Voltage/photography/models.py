from django.db import models

# Create your models here.


class photo_test(models.Model):
    id = models.AutoField(primary_key=True)
    PID = models.CharField(max_length=10)
    name = models.CharField(max_length=80)
    exp = models.CharField(max_length=80)
    des = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    FB = models.CharField(max_length=80)
    fee = models.CharField(max_length=80)

    profile_image = models.CharField(max_length=80)
    sample_image1 = models.CharField(max_length=80)
    sample_image2 = models.CharField(max_length=80)
    sample_image3 = models.CharField(max_length=80)
    sample_image4 = models.CharField(max_length=80)


class meta:
    db_table = "photo_test"


class reservations(models.Model):
    Reservation_ID = models.AutoField(primary_key=True)
    Event_ID = models.CharField(max_length=10)
    S_Time = models.DateTimeField(blank=True, null=True)
    E_Time = models.DateTimeField(blank=True, null=True)
    Resources_ID = models.CharField(max_length=10)

    class meta:
        db_table = "reservations"
