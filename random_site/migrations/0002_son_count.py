# Generated by Django 4.2.8 on 2023-12-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('random_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='son',
            name='count',
            field=models.BooleanField(default=True),
        ),
    ]
