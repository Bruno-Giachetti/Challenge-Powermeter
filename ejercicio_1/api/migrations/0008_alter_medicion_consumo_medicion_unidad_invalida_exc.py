# Generated by Django 4.1.5 on 2023-01-07 19:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_medicion_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicion',
            name='consumo',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddConstraint(
            model_name='medicion',
            constraint=models.CheckConstraint(check=models.Q(('unidad', 'kwh')), name='unidad_invalida_exc'),
        ),
    ]