# Generated by Django 3.2.6 on 2023-05-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230517_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='color',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]
