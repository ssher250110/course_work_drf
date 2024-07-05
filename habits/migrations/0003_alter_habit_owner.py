# Generated by Django 5.0.6 on 2024-07-05 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите создателя привычки', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель привычки'),
        ),
    ]