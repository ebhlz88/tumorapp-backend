# Generated by Django 3.2 on 2021-09-11 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_tumorimage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tumorimage',
            name='name',
        ),
    ]
