# Generated by Django 3.2 on 2021-09-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210911_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='tumorimage',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
