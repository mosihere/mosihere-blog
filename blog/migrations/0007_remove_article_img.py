# Generated by Django 3.2.7 on 2021-09-25 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img',
        ),
    ]
