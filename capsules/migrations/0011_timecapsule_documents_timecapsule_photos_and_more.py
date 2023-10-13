# Generated by Django 4.2.5 on 2023-10-13 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capsules', '0010_alter_document_document_alter_document_time_capsule_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timecapsule',
            name='documents',
            field=models.ManyToManyField(blank=True, related_name='capsules_document', to='capsules.document'),
        ),
        migrations.AddField(
            model_name='timecapsule',
            name='photos',
            field=models.ManyToManyField(blank=True, related_name='capsules_photo', to='capsules.photo'),
        ),
        migrations.AddField(
            model_name='timecapsule',
            name='sounds',
            field=models.ManyToManyField(blank=True, related_name='capsules_sound', to='capsules.sound'),
        ),
        migrations.AddField(
            model_name='timecapsule',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='capsules_video', to='capsules.video'),
        ),
        migrations.AlterField(
            model_name='document',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capsules.timecapsule'),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capsules.timecapsule'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capsules.timecapsule'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capsules.timecapsule'),
        ),
        migrations.AlterField(
            model_name='video',
            name='time_capsule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capsules.timecapsule'),
        ),
    ]