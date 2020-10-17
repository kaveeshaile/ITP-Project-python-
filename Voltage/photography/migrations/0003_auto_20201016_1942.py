# Generated by Django 3.0.8 on 2020-10-16 14:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0002_auto_20200910_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservations',
            fields=[
                ('Reservation_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Event_ID', models.CharField(max_length=10)),
                ('S_Time', models.DateTimeField(blank=True, null=True)),
                ('E_Time', models.DateTimeField(blank=True, null=True)),
                ('Resources_ID', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='photo_test',
            name='profile_image',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo_test',
            name='sample_image1',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo_test',
            name='sample_image2',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo_test',
            name='sample_image3',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo_test',
            name='sample_image4',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
    ]