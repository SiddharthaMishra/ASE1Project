# Generated by Django 2.1.4 on 2018-12-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainupload', '0002_auto_20181209_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='protected',
            field=models.BooleanField(default=False),
        ),
    ]