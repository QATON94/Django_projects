# Generated by Django 5.0.3 on 2024-03-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='учится'),
        ),
    ]
