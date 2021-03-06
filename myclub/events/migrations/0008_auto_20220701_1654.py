# Generated by Django 3.2.5 on 2022-07-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_venue_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='events'),
        ),
        migrations.AddField(
            model_name='venue',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='venues'),
        ),
    ]
