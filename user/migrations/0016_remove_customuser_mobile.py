# Generated by Django 3.2.7 on 2022-01-25 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_customuser_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='mobile',
        ),
    ]