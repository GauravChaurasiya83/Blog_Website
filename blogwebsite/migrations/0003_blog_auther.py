# Generated by Django 4.2.5 on 2024-02-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogwebsite', '0002_blog_description_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='auther',
            field=models.CharField(default=False, max_length=100),
        ),
    ]