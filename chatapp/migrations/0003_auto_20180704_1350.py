# Generated by Django 2.0.6 on 2018-07-04 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_auto_20180703_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
