# Generated by Django 4.2.11 on 2024-03-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showlist', '0002_show_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='watched',
            field=models.BooleanField(default='False'),
        ),
    ]
