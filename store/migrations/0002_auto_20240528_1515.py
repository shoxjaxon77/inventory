# Generated by Django 3.1.13 on 2024-05-28 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirimlar',
            name='keltirilgan_sana',
            field=models.DateField(default=datetime.date.today),
        ),
    ]