# Generated by Django 3.2.6 on 2023-05-12 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='auto_token',
            new_name='auth_token',
        ),
    ]
