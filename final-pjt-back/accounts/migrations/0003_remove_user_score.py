# Generated by Django 3.2.12 on 2022-05-20 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='score',
        ),
    ]