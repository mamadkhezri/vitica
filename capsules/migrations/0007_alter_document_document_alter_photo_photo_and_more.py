# Generated by Django 4.2.5 on 2023-10-12 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsules', '0006_alter_photo_photo_alter_sound_sound_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='sound',
            field=models.FileField(upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='blog/'),
        ),
    ]
