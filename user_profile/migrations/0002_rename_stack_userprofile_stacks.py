# Generated by Django 4.2.6 on 2023-10-08 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='stack',
            new_name='stacks',
        ),
    ]
