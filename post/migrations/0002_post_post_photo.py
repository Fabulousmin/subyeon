# Generated by Django 2.0.6 on 2018-07-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]