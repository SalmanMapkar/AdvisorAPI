# Generated by Django 3.0.8 on 2020-07-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdvisorAPI', '0002_userdatamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatamodel',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
