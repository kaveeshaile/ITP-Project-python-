from django.db import models

# Create your models here.
class decorationInsert(models.Model):

    
    dec_name=models.Charfield(max_length=100)
    dec_dsc=models.Charfield(max_length=1000)
    dec_img1=models.FileField(upload_to=user_directory_path)
    dec_img2=models.FileField(upload_to=user_directory_path)
    dec_img3=models.FileField(upload_to=user_directory_path)
    dec_img4=models.FileField(upload_to=user_directory_path)
    dec_img5=models.FileField(upload_to=user_directory_path)

    class Meta:
        db_table:"decoration"

    