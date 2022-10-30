# Generated by Django 4.1.2 on 2022-10-30 13:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0018_alter_reservation_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='planner.event', validators=[django.core.validators.MinValueValidator(1, 'Minimum reservation seats is 1 seat.')]),
        ),
    ]
