# Generated by Django 2.0.6 on 2018-07-14 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0004_auto_20180712_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='matching',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='matching',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
