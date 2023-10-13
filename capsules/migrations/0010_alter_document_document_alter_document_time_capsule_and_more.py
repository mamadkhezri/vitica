# Generated by Django 4.2.5 on 2023-10-13 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capsules', '0009_alter_document_document_alter_photo_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='capsules.timecapsule'),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='capsules.timecapsule'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, default='static\\img\\lock.png', null=True, upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='capsules.timecapsule'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='sound',
            field=models.FileField(blank=True, null=True, upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sounds', to='capsules.timecapsule'),
        ),
        migrations.AlterField(
            model_name='timecapsule',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='video',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='capsules.timecapsule'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='blog/'),
        ),
    ]