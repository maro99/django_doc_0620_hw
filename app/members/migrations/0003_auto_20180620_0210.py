# Generated by Django 2.0.6 on 2018-06-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='block_users',
            field=models.ManyToManyField(related_name='block_user', to='members.User'),
        ),
    ]
