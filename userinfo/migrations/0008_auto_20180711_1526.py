# Generated by Django 2.0.6 on 2018-07-11 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0007_remove_userinfo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
