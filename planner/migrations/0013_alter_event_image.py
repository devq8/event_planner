# Generated by Django 4.1.2 on 2022-10-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0012_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
