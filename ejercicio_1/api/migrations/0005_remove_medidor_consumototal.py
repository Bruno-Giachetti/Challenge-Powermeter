# Generated by Django 4.1.5 on 2023-01-07 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_medidor_consumototal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medidor',
            name='consumoTotal',
        ),
    ]
