# Generated by Django 3.2.9 on 2022-11-15 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookiesolver', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='EMAIL',
            new_name='Email',
        ),
    ]
