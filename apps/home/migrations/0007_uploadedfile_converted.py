# Generated by Django 3.2.6 on 2023-05-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_uploadedfile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='converted',
            field=models.BooleanField(default=False),
        ),
    ]
