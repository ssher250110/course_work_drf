# Generated by Django 5.0.6 on 2024-06-29 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='user',
            new_name='owner',
        ),
    ]