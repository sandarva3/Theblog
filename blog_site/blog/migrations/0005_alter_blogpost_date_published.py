# Generated by Django 4.1.3 on 2022-12-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_published',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
