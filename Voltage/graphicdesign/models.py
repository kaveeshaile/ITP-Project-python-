from django.db import models

# Create your models here.
class gdInsert(models.Model):

    
    idgraphicdesignID=models.AutoField(primary_key=True)
    graphicname=models.CharField(max_length=45)
    graphicfee=models.CharField(max_length=45)
    graphicdec=models.CharField(max_length=45)
    graphiccontact=models.CharField(max_length=45)
    graphicemail=models.CharField(max_length=45)
    

    class Meta:
        db_table:"graphicdesign"





        