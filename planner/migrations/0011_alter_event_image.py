# Generated by Django 4.1.2 on 2022-10-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0010_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='../media'),
        ),
    ]