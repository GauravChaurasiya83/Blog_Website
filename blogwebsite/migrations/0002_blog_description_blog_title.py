# Generated by Django 4.2.5 on 2024-02-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogwebsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
