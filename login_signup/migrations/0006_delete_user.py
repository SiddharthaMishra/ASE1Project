# Generated by Django 2.1.2 on 2018-11-18 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]