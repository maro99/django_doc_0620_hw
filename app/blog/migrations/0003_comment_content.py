# Generated by Django 2.0.6 on 2018-06-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
