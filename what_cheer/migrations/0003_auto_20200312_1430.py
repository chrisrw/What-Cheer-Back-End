# Generated by Django 3.0.4 on 2020-03-12 14:30

from django.db import migrations, models
import what_cheer.models


class Migration(migrations.Migration):

    dependencies = [
        ('what_cheer', '0002_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=what_cheer.models.Entry.upload_image_name),
        ),
    ]
