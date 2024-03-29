# Generated by Django 4.2.5 on 2023-10-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsules', '0005_rename_timecapsule_comment_time_capsule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='photo/'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='sound',
            field=models.FileField(upload_to='sound/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/'),
        ),
    ]
