# Generated by Django 4.1.3 on 2022-12-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date update'),
        ),
    ]
