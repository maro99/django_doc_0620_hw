# Generated by Django 2.0.6 on 2018-06-20 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20180620_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='block_users',
            field=models.ManyToManyField(to='members.User'),
        ),
    ]
